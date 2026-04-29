from setuptools import setup, find_packages

# read requirements.txt if it exists
def get_requirements():
    try:
        with open("requirements.txt") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

setup(
    name="automatee_theme",
    version="0.0.1",
    description="Custom Frappe Theme App",
    author="Frank Lembalemba",
    author_email="franklembalemba3@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=get_requirements(),
)