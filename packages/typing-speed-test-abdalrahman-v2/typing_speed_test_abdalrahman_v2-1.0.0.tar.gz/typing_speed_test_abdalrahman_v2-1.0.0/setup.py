from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="typing_speed_test_abdalrahman_v2",  # اسم المشروع في PyPI
    version="1.0.0",
    author="Abdalrahman Wahas",
    author_email="your_email@example.com",  # عدل إلى بريدك
    description="A simple typing speed test game in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abdalrahman_wahas23/typing_speed_test_abdalrahman_v2",  # رابط المشروع
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "typing-speed-test=typing_speed_test_abdalrahman.main:typing_speed_test",
        ],
    },
)
