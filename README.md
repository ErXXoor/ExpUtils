# Experiment Utils

Using for make each seperate experiments as routine.

---

## 1. exp_config

Configrations for each experiments, one configs can be mapped to multiply experiments.

- Name convention: Model_Dataset_serialNumber.(json/yaml)
- Contained Keys:
  - dataset_path
  - eval_dataset_path
  - result_path
  - model_attr
    - input_size
    - { hyperparameter }
  - batch_size
  - epoch
  - learning_rate

## 2. exp_result

Experiment results for each experiments, multiple results can be mapped to single config.

- Name convention: {ConfigName}_serialNumber.json
- Contained Keys:
  - train_log
    - dataset_size
    - dataload_duration
    - train_duration
  - evaluate_log
    - dataset_size
    - dataload_duration
    - evaluate_duration
