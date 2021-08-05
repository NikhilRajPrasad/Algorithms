# This Algorithm was designed by Nikhil Raj Prasad on 04/08/21.
def le(left):
    suml=0;
    while(bool(left)):
        z=max(left);
        m=left.index(z);
        suml=suml+z;
        if(m==0):
            if(m!=len(left)-1):
                left.remove(left[m+1]);
            left.remove(z);
        else:
            l=left[m-1];
            try:
                h=left[m+1];
                left.remove(h);
            except IndexError:
                pass;
            left.remove(z);
            left.remove(l);
    return suml;
def Ri(right):
    sumr=0;
    while(bool(right)):
        z=max(right);
        m=right.index(z);
        sumr=sumr+z;
        if(m==0):
            if(m!=len(right)-1):
                right.remove(right[m+1]);
            right.remove(z);
        else:
            l=right[m-1];
            try:
                h=right[m+1];
                right.remove(h);
            except IndexError:
                pass;
            right.remove(z);
            right.remove(l);
    return sumr;        


if __name__=="__main__":
    k=[2,7,10,3,1,45,21,56,78,34,90,76,39];
    z=max(k);
    Sum=z;
    i=k.index(z);
    o=i;
    if i>=2:
        left=k[:i-1]
    else:
        left=[];

    if o<=len(k)-2:
        right=k[o+2:len(k)]
    else:
        right=[];
        
    Sum=Sum+le(left)+Ri(right);
    print(Sum);