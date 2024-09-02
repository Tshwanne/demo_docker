# ---------------------------------------------------------------------------- #
#                                    Schemas                                   #
# ---------------------------------------------------------------------------- #
TRAIN_SCHEMA = {
    'data_url': {
        'type': str,
        'required': True
    },
    'hf_model': {
        'type': str,
        'required': False,
        'default': None
    },
    'hf_token': {
        'type': str,
        'required': False,
        'default': None
    },
    'ckpt_link': {
        'type': str,
        'required': False,
        'default': None
    },
    'concept_name': {
        'type': str,
        'required': False,
        'default': None
    },
    'offset_noise': {
        'type': bool,
        'required': False,
        'default': False
    },
    'pndm_scheduler': {
        'type': bool,
        'required': False,
        'default': False
    },
    # Text Encoder Training Parameters
    'text_steps': {
        'type': int,
        'required': False,
        'default': 350
    },
    'text_seed': {
        'type': int,
        'required': False,
        'default': 555
    },
    'text_batch_size': {
        'type': int,
        'required': False,
        'default': 1
    },
    'text_resolution': {
        'type': int,
        'required': False,
        'default': 512
    },
    'text_learning_rate': {
        'type': float,
        'required': False,
        'default': 1e-6
    },
    'text_lr_scheduler': {
        'type': str,
        'required': False,
        'default': 'linear',
        'constraints': lambda scheduler: scheduler in ['linear', 'cosine', 'cosine_with_restarts', 'polynomial', 'constant', 'constant_with_warmup']
    },
    'text_8_bit_adam': {
        'type': bool,
        'required': False,
        'default': False
    },
    # UNet Training Parameters
    'unet_seed': {
        'type': int,
        'required': False,
        'default': 555
    },
    'unet_batch_size': {
        'type': int,
        'required': False,
        'default': 1
    },
    'unet_resolution': {
        'type': int,
        'required': False,
        'default': 512
    },
    'unet_epochs': {
        'type': int,
        'required': False,
        'default': 150
    },
    'unet_learning_rate': {
        'type': float,
        'required': False,
        'default': 2e-6
    },
    'unet_lr_scheduler': {
        'type': str,
        'required': False,
        'default': 'linear',
        'constraints': lambda scheduler: scheduler in ['linear', 'cosine', 'cosine_with_restarts', 'polynomial', 'constant', 'constant_with_warmup']
    },
    'unet_8_bit_adam': {
        'type': bool,
        'required': False,
        'default': False
    }
}

