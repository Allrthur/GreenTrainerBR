# Towards Golden Green AI

## Introduction
This is an exploration of the technique proposed in ["Towards Green AI in Fine-tuning Large Language Models via Adaptive Backpropagation"](https://arxiv.org/abs/2309.13192) while fine tuning brazilian portuguese generative models.

## Requirements
All the experiments are run on Lambda Cloud Instances. To install all the dependencies, run the following command
```
bash requirements.sh
```
## General Usage
For decoder structures, navigate to `decoder_lm` folder. Run the following commands to finetune

```
bash opt_scitldr.sh # finetune OPT-2.7B model on scitldr dataset
bash opt_dialogsum.sh # finetune OPT-2.7B model on scitldr dataset
```

or pass specific configurations to main.py

```
# GreenTrainer-0.5
python3 main.py --model_name facebook/opt-2.7b \
                --dataset_name scitldr \
                --scheme green_trainer \
                --max_input_length 512 \
                --max_output_length 64 \
                --batch_size 4 \
                --rho 0.4
```

For encoder-decoder structures, navigate to `encoder_decoder_lm`. Follow similar steps above.

## Reproducing Paper Results
Most of experiments in our paper are run on a Lambda Cloud Instance with a single Nvidia H100 80GB GPU and 24 vCPUs. If you select other configurations, the wall-clock time measurements will not match the results in our paper. Please run the following scripts to reproduce main results for OPT-2.7B, BLOOMZ-3B, and FLAN-T5-3B respectively:

Navigate to `decoder_lm` folder,
```
# finetuning OPT-2.7B on SciTLDR and DialogSum datasets
bash opt_scitldr.sh
bash opt_dialogsum.sh

# finetuning BLOOMZ-3B on SciTLDR and DialogSum datasets
bash bloom_scitldr.sh
bash bloom_dialogsum.sh

# finetuning OPT-2.7B on webquestions and piqa datasets
bash opt_webquestions.sh
bash opt_piqa.sh
```
Nvigate to `encoder_decoder_lm` folder,
```
# finetuning FLAN-T5-3B on SciTLDR and DialogSum datasets
bash flant5_scitldr.sh
bash flant5_dialogsum.sh
```
**Note:** For OPT and BLOOMZ, we adopt prompt structure `{src} TL;DR: {summary}` on SciTLDR and DialogSum datasets, `question:{q}</s>answer:{a}</s>` on webquestions dataset, and `goal:{goal}</s>sol1:{sol1}</s>sol2:{sol2}</s>label:{label}</s>` on piqa dataset. For summarization datasets, `{src} TL;DR: {summary}</s>` should give better results but we didn't adopt this when writing this paper. 

## Citation
```
@article{huang2023towards,
  title={Towards Green AI in Fine-tuning Large Language Models via Adaptive Backpropagation},
  author={Huang, Kai and Yin, Hanyun and Huang, Heng and Gao, Wei},
  journal={arXiv preprint arXiv:2309.13192},
  year={2023}
}
```

