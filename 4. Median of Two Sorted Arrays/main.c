double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
   
    int totalSize = nums1Size + nums2Size;
   
    float* concan = (float *)malloc(totalSize * sizeof(float));

    for(int i = 0; i < nums1Size; i++)
        *(concan + i) = *(nums1 + i);
    for(int i = 0; i < nums2Size; i++)
        *(concan+i+nums1Size) = *(nums2 + i);

    int temp;
    /*going to sort  the array in ascending order using 2 for loops*/
    for(int i=0; i<totalSize; i++) {
        for(int j = i+1; j < totalSize; j++){
            if (*(concan+i)>*(concan+j)) {
                temp = *(concan+j);
                *(concan+j)=*(concan+i);
                *(concan+i)=temp;
            }
        }
    }

   
    double median = 0;

    (totalSize % 2==0) ? (median = ((*(concan+(totalSize/2)) + *(concan+((totalSize/2)-1)))/2)): (median = *(concan+(totalSize)/2));
        


    return median;
}
