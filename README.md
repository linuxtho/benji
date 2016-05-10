benji
=====
A module-based IRC robot created by the DigitalAddiction community. Woof.

Installing
==========
This should get you going with a [virtualenv](https://virtualenv.pypa.io/en/latest/)
environment:
```bash
virtualenv env
pip install -r requirements.txt
source env/bin/activate
python setup.py
```

Docker builds coming soon :)

Adding Modules
=============
The module interface is still under works... We'll update this when things
have been worked out!

Contributing
============
We love pull requests!

Contributions will be automatically built into the bot running on
irc.digitaladdiction.info, so we are a mildly cautious about accepted
changes. Your pull requests should pass flake8 checks to ensure code quality.
Additionally, all changes will be run through a testing environment to ensure
that they will not disrupt the integrity of the IRC channels within which they
will live.
