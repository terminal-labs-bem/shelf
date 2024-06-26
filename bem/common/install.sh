export INSTALLUSER=$1
source .tmp/_commonenv.sh

echo "username"
echo $INSTALLUSER
echo "trying to install"

mkdir -p /home/$INSTALLUSER/.tlcache/bem/$APPNAME
mkdir -p /home/$INSTALLUSER/.tlcache/bem/$APPNAME/vars
chown -R $INSTALLUSER $FILE /home/$INSTALLUSER/.tlcache

bash .tmp/bem/common/pattern/superuser/deps.sh

sudo su $INSTALLUSER <<'EOF'
  curl https://sh.rustup.rs -sSf | sh -s -- -y
  curl -sSf https://rye-up.com/get | RYE_VERSION="0.32.0" RYE_TOOLCHAIN_VERSION="3.11.8" RYE_INSTALL_OPTION="--yes" bash

  source .tmp/_commonenv.sh
  me="$(whoami)"
  bash .tmp/bem/common/pattern/user/stage.sh $me
  bash .tmp/bem/common/pattern/user/emit.sh $me
  bash .tmp/bem/common/pattern/user/run.sh $me
EOF
