# Uploading

Do to following to set up the readme:

1) use nbconvert to convert ./README.ipynb to README.md and README.rst

    ipython nbconvert --to markdown ./README.ipynb
    ipython nbconvert --to rst ./README.ipynb

2) Test the restructured text using python setuptools

    python setup.py --long-description | rst2html.py > output.html
    open output.html


