#include<iostream>

using namespace std;

int encrypt(int input){

    int start, end, range;
    int output; int wrap;

    if(islower(input)){
        start='a';
        end='z';
    }
    if(isupper(input)){
        start='A';
        end= 'Z';
    }
    if(isdigit(input)){
        start='0';
        end='9';
    }

    range = end - start + 1;

    output = input - (6 % range);                                                                                       
    
    wrap = start - output;                                                                                                                                                                                                                                                           if (wrap > 0)                                                                                                              
    if(wrap>0){
        output = end + 1 - wrap;
    }                                                                                  
    
    return output;


}



int main(){

    string s="eK5ranw5MfKsztLBe6K0";

    for(int i=0; i<s.size(); i++){
        printf("%c",encrypt(s[i]));
    }
    cout<<'\n';


    return 0;
}