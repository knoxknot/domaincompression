#### Installation and Usage Guide
```shell
git clone https://github.com/knoxknot/domaincompression  # git clone the repository
cd dns-notation  # change into directory
pip install -r requirements.txt  # install dependencies
pyinstaller --onefile domaincompression.py --distpath $HOME/.local/bin/ --name domaincompression  # build and install domaincompression
```
