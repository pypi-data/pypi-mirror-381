import numpy as np
import pytest
import os
import shutil
from sklearn.preprocessing import StandardScaler

from sdg_core_lib.NumericDataset import NumericDataset
from sdg_core_lib.data_generator.models.TrainingInfo import TrainingInfo
from sdg_core_lib.data_generator.models.keras.VAE import VAE
from sdg_core_lib.data_generator.models.keras.implementation.TabularVAE import (
    TabularVAE,
)


@pytest.fixture()
def data():
    return NumericDataset(
        [
            {
                "column_name": "A",
                "column_type": "continuous",
                "column_datatype": "float64",
                "column_data": [1.0, 2.0, 3.0, 4.0, 5.0],
            }
        ]
    )


@pytest.fixture()
def model_data_no_load():
    return {
        "metadata": {"example_key": "example_value"},
        "model_name": "example_model",
        "input_shape": "(13,)",
        "load_path": None,
        "epochs": 1,
    }


@pytest.fixture()
def model_data_correct_train():
    return {
        "metadata": {"example_key": "example_value"},
        "model_name": "example_model",
        "input_shape": "(1,)",
        "load_path": None,
        "epochs": 1,
    }


def test_instantiate(model_data_no_load):
    model = TabularVAE(**model_data_no_load)
    assert model.model_name == model_data_no_load["model_name"]
    assert model._load_path is None
    assert model.input_shape == (13,)
    assert model._epochs == 1
    assert type(model._model) is VAE
    assert model._scaler is None


def test_preprocess(model_data_no_load, data):
    model = TabularVAE(**model_data_no_load)
    assert model._scaler is None
    scaled_data = model._pre_process(data)
    assert model._scaler is not None and type(model._scaler) is StandardScaler
    assert type(scaled_data) is np.ndarray


def test_self_description(model_data_no_load):
    model = TabularVAE(**model_data_no_load)
    self_description = model.self_describe()
    assert self_description is not None
    assert (
        self_description["algorithm"]["name"]
        == "sdg_core_lib.data_generator.models.keras.implementation.TabularVAE.TabularVAE"
    )
    assert self_description["algorithm"]["default_loss_function"] == "ELBO LOSS"
    assert (
        self_description["algorithm"]["description"]
        == "A Variational Autoencoder for data generation"
    )
    assert self_description["datatypes"] == [
        {"type": "float32", "is_categorical": False},
        {"type": "int32", "is_categorical": False},
        {"type": "int64", "is_categorical": False},
    ]


def test_save(model_data_no_load):
    model = TabularVAE(**model_data_no_load)
    model_path = "./test_model"
    os.mkdir(model_path)
    model.save(model_path)
    assert os.path.isfile(os.path.join(model_path, "encoder.keras"))
    assert os.path.isfile(os.path.join(model_path, "decoder.keras"))
    assert os.path.isfile(os.path.join(model_path, "scaler.skops"))
    shutil.rmtree(model_path)


def test_train_wrong(model_data_no_load, data):
    model = TabularVAE(**model_data_no_load)
    with pytest.raises(ValueError) as exception_info:
        model.train(data)
    assert exception_info.type is ValueError


def test_train_correct(model_data_correct_train, data):
    model = TabularVAE(**model_data_correct_train)
    assert model.training_info is None
    assert model._scaler is None
    model.train(data)
    assert type(model._scaler) is StandardScaler
    assert type(model.training_info) is TrainingInfo


def test_infer(model_data_correct_train, data):
    n_rows = 2
    model = TabularVAE(**model_data_correct_train)
    results = model.infer(n_rows)
    assert results.shape == (n_rows, *model.input_shape)
