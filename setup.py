from setuptools import setup

setup(
    name="model_predictor",
    version="1.0.0",
    python_requires=">=3.6",
    packages=["Model"],  # Manually specify your package
    include_package_data=True,  # Include non-code files
    package_data={
        "Model": ["model_pickle"]  # Ensure pickle file is included
    },
)
