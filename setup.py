from setuptools import setup, find_packages

setup(
    name = "mc_wordcloud",
    version = "0.0.1",
    author = "魔扣少儿编程",
    url = "https://github.com/LucasKKK/mc_wordcloud"
    packages = find_packages(),
    include_package_date = True,
    install_requires = ['wordcloud', 'numpy', 'matplotlib', 'pillow']
)
