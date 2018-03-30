"""

You are given two sorted arrays that contain only integers.
Your task is to find a way to merge them into a single one,
sorted in ascending order.
Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.

You don't need to worry about validation,
since arr1 and arr2 must be arrays with 0 or more Integers.
If both arr1 and arr2 are empty, then just return an empty array.

Note: arr1 and arr2 may be sorted in different orders.
Also arr1 and arr2 may have same integers.
Remove duplicated in the returned result.

Examples
arr1 = [1, 2, 3, 4, 5];
arr2 = [6, 7, 8, 9, 10];
mergeArrays(arr1, arr2);  // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr3 = [1, 3, 5, 7, 9];
arr4 = [10, 8, 6, 4, 2];
mergeArrays(arr3, arr4);  // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr5 = [1, 3, 5, 7, 9, 11, 12];
arr6 = [1, 2, 3, 4, 5, 10, 12];
mergeArrays(arr5, arr6);  // [1, 2, 3, 4, 5, 7, 9, 10, 11, 12]

"""



def merge_arrays(arr1, arr2)
  arr1.concat arr2
  return arr1.uniq.sort
end


describe "merge_arrays" do
  context "given [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]" do
    it "returns [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" do
      expect(merge_arrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])).to eq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    end
  end

  context "given [1, 3, 5, 7, 9], [10, 8, 6, 4, 2]" do
    it "returns [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" do
      expect(merge_arrays([1, 3, 5, 7, 9], [10, 8, 6, 4, 2])).to eq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    end
  end


end