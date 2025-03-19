int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = (int*) malloc(100 * sizeof(int));
    for(int i = 0; i < numsSize; i++){
        for(int j = 0; j < numsSize; j++) {
            if((*(nums + i) + *(nums + j)) == target && i != j){
                result[0] = i;
                result[1]= j;
                  *returnSize = 2;
