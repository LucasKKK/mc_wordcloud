import setuptools

setuptools.setup(
    name = "mc_wordcloud",
    version = "0.0.1",
    author = "魔扣少儿编程",
    author_email = "2443927272@qq.com",
    url = "https://github.com/LucasKKK/mc_wordcloud",
    packages = setuptools.find_packages(),
    #include_package_date = True,
    install_requires = ['wordcloud', 'numpy', 'matplotlib', 'pillow']
)
