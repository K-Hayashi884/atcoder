# $1=cource name(lower case)
# $2=number

make_files(){
    dir=`echo $1 | tr '[a-z]' '[A-Z]'`
    display_num=`printf %03d $2`
    if [ ! -e $dir ]; then mkdir $dir ; fi
    cd $dir
    if [ ! -e $1$display_num ];then
        mkdir $1$display_num
        cd $1$display_num
        touch input.txt
        L=(A B C D E F)
        for var in ${L[@]}
        do
            touch "$1${display_num}$var.py"
        done
    fi
}
make_files $1 $2