'''
Nvidia: Building Transformer-Based Natural Language Processing Applications
'''

from nemo.collections import nlp as nemo_nlp
from nemo.utils.exp_manager import exp_manager

import torch
import pytorch_lightning as pl
from omegaconf import OmegaConf

# Instantiate the OmegaConf object by loading the config file
TC_DIR = "/dli/task/nemo/examples/nlp/text_classification"
CONFIG_FILE = "text_classification_config.yaml"
config = OmegaConf.load(TC_DIR + "/conf/" + CONFIG_FILE) # config .yaml file -> object with .attributes 

# set the config values using omegaconf
# on model
config.model.optim.lr = 5.0e-05
config.model.dataset.num_classes = 3
config.model.dataset.max_seq_length = 128
config.model.train_ds.file_path = "/dli/task/data/NCBI_tc-3/train_nemo_format.tsv"
config.model.validation_ds.file_path = "/dli/task/data/NCBI_tc-3/train_nemo_format.tsv"
config.model.test_ds.file_path = "/dli/task/data/NCBI_tc-3/test_nemo_format.tsv"
config.model.infer_samples = ["Germline mutations in BRCA1 are responsible for most cases of inherited breast and ovarian cancer ",
        "The first predictive testing for Huntington disease  was based on analysis of linked polymorphic DNA markers to estimate the likelihood of inheriting the mutation for HD",
        "Further studies suggested that low dilutions of C5D serum contain a factor or factors interfering at some step in the hemolytic assay of C5 rather than a true C5 inhibitor or inactivator"]

# on trainer
config.trainer.max_epochs = 5
config.trainer.amp_level = '01'
config.trainer.precision = 16

# Instantiate the trainer and experiment manager
trainer = pl.Trainer(**config.trainer)
exp_manager(trainer, config.exp_manager)
model = nemo_nlp.models.TextClassificationModel(config.model, trainer=trainer)

# start model training and save result
# The training takes about 2 minutes to run
trainer.fit(model)
model.save_to(config.model.nemo_path)

trainer.test(model=model, verbose=False)

print(config.model.infer_samples)

model.classifytext(queries=config.model.infer_samples, batch_size=64, max_seq_length=128)
