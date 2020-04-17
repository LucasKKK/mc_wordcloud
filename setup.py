import setuptools
setuptools.setup(
    name = "mc_wordcloud",
    version = "0.0.6",
    author = "魔扣少儿编程",
    author_email = "2443927272@qq.com",
    url = "https://github.com/LucasKKK/mc_wordcloud", 
    data_files = [('mc_wordcloud', [
        'mc_wordcloud/鲁班.jpg',
        'mc_wordcloud/鲁班.txt'
    ])
    ],
    packages = ['mc_wordcloud'],     #多个文件夹手动添加
    include_package_data = True,
    #packages = setuptools.find_packages(),
    install_requires = ['wordcloud', 'numpy', 'matplotlib', 'pillow']
)
