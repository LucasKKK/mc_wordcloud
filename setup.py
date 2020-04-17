import setuptools
setuptools.setup(
    name = "mc_wordcloud",
    version = "0.0.8",
    author = "魔扣少儿编程",
    author_email = "2443927272@qq.com",
    url = "https://github.com/LucasKKK/mc_wordcloud", 
    data_files = [('mc_wordcloud', [
        'mc_wordcloud/百里守约.jpg',
        'mc_wordcloud/百里守约.txt',
        #'mc_wordcloud/程咬金.jpg',  x
        #'mc_wordcloud/程咬金.txt',
        #'mc_wordcloud/狄仁杰.jpg',  x
        #'mc_wordcloud/狄仁杰.txt',
        'mc_wordcloud/貂蝉.jpg',
        'mc_wordcloud/貂蝉.txt',
        #'mc_wordcloud/宫本武藏.jpg',x
        #'mc_wordcloud/宫本武藏.txt',
        'mc_wordcloud/韩信.jpg',
        'mc_wordcloud/韩信.txt',
        #'mc_wordcloud/花木兰.jpg', x
        #'mc_wordcloud/花木兰.txt',
        'mc_wordcloud/李白.jpg',
        'mc_wordcloud/李白.txt',
        'mc_wordcloud/鲁班.jpg',
        'mc_wordcloud/鲁班.txt',
        'mc_wordcloud/上官婉儿.jpg',
        'mc_wordcloud/上官婉儿.txt'
        #'mc_wordcloud/孙悟空.jpg',x
        #'mc_wordcloud/孙悟空.txt'
    ])
    ],
    packages = ['mc_wordcloud'],     #多个文件夹手动添加
    include_package_data = True,
    #packages = setuptools.find_packages(),
    install_requires = ['wordcloud', 'numpy', 'matplotlib', 'pillow']
)
