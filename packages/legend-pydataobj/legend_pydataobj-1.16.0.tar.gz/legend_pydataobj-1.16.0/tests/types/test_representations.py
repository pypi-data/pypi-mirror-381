from __future__ import annotations

import numpy as np

import lgdo

rng = np.random.default_rng()


def test_representations():
    objs = {
        "Scalar": lgdo.Scalar("test", attrs={"unit": "ns"}),
        "Array1": lgdo.Array(rng.random(3), attrs={"unit": "ns"}),
        "Array2": lgdo.Array(rng.random(10), attrs={"unit": "ns"}),
        "Array3": lgdo.Array(rng.random(100), attrs={"unit": "ns"}),
        "ArrayOfEqualSizedArrays": lgdo.ArrayOfEqualSizedArrays(
            nda=rng.random((10, 100)), attrs={"unit": "ns"}
        ),
        "Struct": lgdo.Struct(
            {
                "first": lgdo.Array(rng.random(100), attrs={"unit": "ns"}),
                "second": lgdo.Scalar(3.45, attrs={"unit": "ns"}),
                "third": lgdo.Array(rng.random(3), attrs={"unit": "ns"}),
                "fourth": lgdo.ArrayOfEqualSizedArrays(
                    nda=rng.random((10, 100)), attrs={"unit": "ns"}
                ),
            },
            attrs={"unit": "ns"},
        ),
        "VectorOfVectors": lgdo.VectorOfVectors(
            flattened_data=lgdo.Array(rng.random(1000)),
            cumulative_length=lgdo.Array(np.array([5, 12, 34, 49, 150])),
            attrs={"unit": "ns"},
        ),
        "VectorOfEncodedVectors": lgdo.VectorOfEncodedVectors(
            encoded_data=lgdo.VectorOfVectors(
                flattened_data=lgdo.Array(rng.integers(255, size=1000, dtype="ubyte")),
                cumulative_length=lgdo.Array(np.array([5, 12, 34, 49, 150])),
                attrs={"unit": "ns"},
            ),
            decoded_size=lgdo.Array(shape=5, fill_val=56),
            attrs={"codec": "radware-sigcompress", "codec_shift": 123},
        ),
        "ArrayOfEncodedEqualSizedArrays": lgdo.ArrayOfEncodedEqualSizedArrays(
            encoded_data=lgdo.VectorOfVectors(
                flattened_data=lgdo.Array(rng.integers(255, size=1000, dtype="ubyte")),
                cumulative_length=lgdo.Array(np.array([5, 12, 34, 49, 150])),
                attrs={"unit": "ns"},
            ),
            decoded_size=56,
            attrs={"codec": "radware-sigcompress", "codec_shift": 123},
        ),
        "Table": lgdo.Table(
            col_dict={
                "first": lgdo.Array(rng.random(100), attrs={"unit": "ns"}),
                "second": lgdo.Array(rng.random(100)),
                "third": lgdo.Array(rng.random(100), attrs={"unit": "ns"}),
            },
            attrs={"greeting": "ciao"},
        ),
        "WaveformTable1": lgdo.WaveformTable(
            values=lgdo.VectorOfVectors(
                flattened_data=lgdo.Array(rng.random(1000)),
                cumulative_length=lgdo.Array(np.array([5, 12, 74, 230])),
            ),
            attrs={"greeting": "ciao"},
        ),
        "WaveformTable2": lgdo.WaveformTable(
            values=lgdo.ArrayOfEqualSizedArrays(nda=rng.random((10, 1000))),
            attrs={"greeting": "ciao"},
        ),
        "WaveformTable3": lgdo.WaveformTable(
            values=lgdo.ArrayOfEqualSizedArrays(nda=rng.random((10, 100))),
            attrs={"greeting": "ciao"},
        ),
    }

    for k, it in objs.items():
        print(f">>> {k} (__repr__)")
        print(repr(it))
        print()
        print(f">>> print({k}) (__str__)")
        print(it)
        print()
