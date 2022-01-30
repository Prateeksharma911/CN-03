
if [ $# -ne 1 ]; then
  echo "Use: $(basename $0) 'word '"
  exit 1
fi

curl=$(which curl)
outfile="output.txt"
word=${1^}
url="https://en.wikipedia.org/wiki/$word"
echo "URL: "$url
echo $url >> logforbash.txt
htmlresult="$(curl $url)"

function strip_html(){
    result="$(grep -m 1 "<p>" <<< $htmlresult | sed 's/<[^>]*>//g')"
    echo $result
    
}
strip_html