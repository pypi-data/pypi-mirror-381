from setuptools import setup

setup(
    name="diabetes-analysis-malk-alobiedy",
    version="0.1.1",
    py_modules=["diabetes_analysis_malk_alobiedy"],  # بدون .py
    install_requires=[
        "pandas",
        "scikit-learn"
    ],
    author="Waleed Alobiedy",
    description="A package for diabetes analysis",
)
