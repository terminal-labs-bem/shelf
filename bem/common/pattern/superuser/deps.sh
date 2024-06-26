DEBIAN_FRONTEND=noninteractive
echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
sudo apt-get install -y -q

if [  -n "$(uname -a | grep Ubuntu)" ]; then
	apt-get update
	apt-get install software-properties-common -y
	add-apt-repository ppa:deadsnakes/ppa -y
else
    apt-get update
fi 

apt-get update
apt-get install build-essential curl -y
apt-get install python3.11 -y
apt-get install python3.11-venv -y
apt-get install git -y

apt-get install lsb-release software-properties-common gnupg -y
wget https://apt.llvm.org/llvm.sh
chmod u+x llvm.sh
./llvm.sh 17

apt-get install clang-17 lldb-17 lld-17 -y
apt-get install libllvm-17-ocaml-dev libllvm17 llvm-17 llvm-17-dev llvm-17-doc llvm-17-examples llvm-17-runtime -y
apt-get install clang-17 clang-tools-17 clang-17-doc libclang-common-17-dev libclang-17-dev libclang1-17 clang-format-17 python3-clang-17 clangd-17 clang-tidy-17 -y
apt-get install clang-17 lldb-17 lld-17 clangd-17 clang-tidy-17 clang-format-17 clang-tools-17 llvm-17-dev lld-17 lldb-17 llvm-17-tools libomp-17-dev libc++-17-dev libc++abi-17-dev libclang-common-17-dev libclang-17-dev libclang-cpp17-dev libunwind-17-dev libclang-rt-17-dev libpolly-17-dev -y
apt-get install libc++-17-dev libc++abi-17-dev -y
apt-get install flang-17 -y

ln -s /usr/bin/clang-17 /usr/bin/clang
update-alternatives --install /usr/bin/cc cc /usr/bin/clang 100
update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++ 100
