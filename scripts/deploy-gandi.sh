
user=9101724
host=git.sd5.gpaas.net
homedir=/vhosts/default


echo "## Pushing repo to Gandi"
git push gandi master

echo "## Cleaning and deploying on Gandi"
# ssh $user@$host clean default.git
ssh $user@$host deploy default.git

echo "## Copying secrets.py to Gandi"
scp mysecrets.py $user@$host:$homedir 
