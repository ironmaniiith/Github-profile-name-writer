echo 'Enter the repo name'
read repo
echo 'Enter the username'
read username
echo 'Enter the access token'
read token
name='abcdefghijklmnopqrstuvwxyz'
for i in `echo $name | grep -o .`
do
curl -i -H "Authorization: token $token" -d "{ \"name\": \"$repo\",\"auto_init\": true, \"private\": false }" https://api.github.com/user/repos
echo 'Go have a look and come back'
read temp
# echo "The repo with the name "$repo" is going to be deleted, make sure that you know what you are doing"
read temp
echo 'Tata bye bye '
curl -i -X DELETE -H "Authorization: token $token" https://api.github.com/repos/$username/$repo
done