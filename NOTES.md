# Uploading

Do to following to set up the readme:

1) use nbconvert to convert ;/README.ipynb to README.md and README

    ipython nbconvert --to markdown ./README.ipynb
    ipython nbconvert --to rst ./README.ipynb
    rst2html.py README.rst > output.html
    open output.html
    mv ./README.rst README
    rm output.html

2) Test the restructured text using python setuptools

    python setup.py --long-description | rst2html.py > output.html
    open output.html

3) When changing versions, you need to add a new tag to git

    git tag 0.4 -m "here is a tag message"
    git push --tag

4) Now register and upload to PyPI

    python setup.py register -r pypi
    python setup.py sdist upload -r pypi


# References
http://peterdowns.com/posts/first-time-with-pypi.html
http://tom-christie.github.io/articles/pypi/
