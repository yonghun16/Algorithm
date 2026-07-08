// https://programmers.co.kr/learn/courses/30/lessons/12977

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int nums[], size_t nums_len) {
    int answer = 0;
    for(int i=0; i<nums_len-2; i++){
        for(int j=i+1; j<nums_len-1; j++){
            for(int k=j+1; k<nums_len; k++){
                if(lsPrime(nums[i], nums[j], nums[k])){
                    answer++;
                }
            }
        }
    }
    return answer;
}

int lsPrime(int a, int b, int c){
    int sum = a + b + c;
    for(int i=sum-1; i>1; i--){
        if(sum%i == 0){
            return false;
        }
    }
    return true;
}
