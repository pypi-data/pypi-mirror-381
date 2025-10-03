import numpy as np
import torch
from raySD.utils.Enable_xFormers import *
from raySD.pipeline.Abstract_Pipeline import *
from raySD.prompt.pencil_art_prompt import *
from raySD.modules.sd_hijack_clip import *
from raySD.pydantic_model.Stable_Diffusion_Lineart_Hijack_Model import *
from raySD.utils.Lineart_Standard import *
from raySD.utils.Preprocess_Resize_Image import *
import time
import cv2
from PIL import Image
import importlib

class StableDiffusionLineartHijackPipeline(AbstractPipeline):
    def __init__(self, **kwargs):
        super().__init__()
        ## Config
        self.config = SD_Lineart_Hijack_Config(**kwargs)

    def update_params_infer(self, **kwargs):
        self.config.inference_steps = kwargs.get("inference_steps", 20)
        self.config.guidance_scale = kwargs.get("guidance_scale", 7)
        self.config.ip_adapter_scale = kwargs.get("ip_adapter_scale", 1)
        self.config.clip_skip = kwargs.get("clip_skip", 2)
        self.config.num_images_per_prompt = kwargs.get("num_images_per_prompt", 1)

    def load_weights(self):
        from diffusers import DPMSolverMultistepScheduler  
        from diffusers import StableDiffusionPipeline
        from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
        from controlnet_aux import TEEDdetector, LineartDetector

        ## Device
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"DEVICE: {self.device}")

        ## Load TEED detector
        self.teed_detector = TEEDdetector.from_pretrained(pretrained_model_or_path=self.config.teed_detector_path, filename=self.config.teed_model_name)

        ## Load Lineart detector
        try:
            self.lineart_detector = LineartDetector.from_pretrained(pretrained_model_or_path=self.config.lineart_detector_path, filename=self.config.lineart_model_name)
        except Exception as e:
            print(f"Error loading LineartDetector: {e}")
            print("Load from pretrained...")
            self.lineart_detector = LineartDetector.from_pretrained("lllyasviel/Annotators")

        ## Load ControlNet
        ### Control TEED
        control_teed = ControlNetModel.from_single_file(self.config.control_teed_path, torch_dtype=torch.float16).to(self.device)

        ## Control Lineart
        control_line_art = ControlNetModel.from_single_file(self.config.control_lineart_path, torch_dtype=torch.float16).to(self.device)

        ## Load Stable Diffusion model
        self.pipeline = StableDiffusionControlNetPipeline.from_single_file(
            self.config.checkpoint_path,
            controlnet=[control_teed, control_line_art],
            torch_dtype=torch.float16,
            safety_checker=None
        ).to(self.device)

        ### Scheduler
        self.pipeline.scheduler = DPMSolverMultistepScheduler.from_config(
            self.pipeline.scheduler.config,
            algorithm_type="dpmsolver++",       # <-- DPM++
            use_karras_sigmas=True,             # <-- Karras
            solver_order=2                      # <-- 2M (2nd order multistep)
        )

        if self.config.lora_style_path:
            self.pipeline.load_lora_weights(self.config.lora_style_path)

        enable_xformers_if_available(self.pipeline)

        print("LOAD SD PIPELINE DONE")
        
        print("Begin hijack CLIP text encoder...")

        self.hijack_text_encoder = DiffusersHijackTextEncoder(
            text_encoder=self.pipeline.text_encoder,
            tokenizer=self.pipeline.tokenizer,
            chunk_length=75,  # như A1111
            comma_padding_backtrack=5,  # giống A1111
        )
        self.hijack_text_encoder = self.hijack_text_encoder.to(self.device)

        print("Hijack CLIP text encoder done.")

    def forward(self, x: Image.Image, *args, **kwargs):
        gender = kwargs["gender"]
        age = kwargs["age"]
        resize_mode = kwargs["resize_mode"]

        ## Resize & crop if needed
        if resize_mode >= 0 and resize_mode <= 2:
            x = preproces_resize_image(resize_mode, x, self.config.width, self.config.height)
        
        I_gray = x.convert("L").convert("RGB")
        teed_image = self.teed_detector(I_gray, detect_resolution=self.config.res_ref)
        lineart_image = self.lineart_detector(I_gray, detect_resolution=self.config.res_ref)

        if self.config.style_name == "pencil_art":
            pencil_art_prompt = PencilArtPrompt(gender=gender)
            self.prompt, self.negative_prompt = pencil_art_prompt.get_prompt(is_list=True)

        start_time = time.time()
        with torch.no_grad():
            prompt_embed = self.hijack_text_encoder(self.prompt)
            negative_prompt_embed = self.hijack_text_encoder(self.negative_prompt)

        image = self.pipeline(
            prompt_embeds=prompt_embed,
            negative_prompt_embeds=negative_prompt_embed,
            image=[teed_image, lineart_image],
            guidance_scale=self.config.guidance_scale,
            num_inference_steps=self.config.inference_steps,
            controlnet_conditioning_scale=[self.config.control_teed_scale, self.config.control_lineart_scale],
            num_samples=self.config.num_images_per_prompt,
            width=self.config.width,
            height=self.config.height
        )[0][0]
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        return image
        