class KthLargest {
     PriorityQueue<Integer> minHeap; 
 int k;

 public KthLargest(int k, int[] nums) {
  minHeap = new PriorityQueue<>();
  this.k = k;
  for(int val: nums) {
   if(minHeap.size()<k||val>minHeap.peek()) minHeap.add(val);
   if(minHeap.size()>k) minHeap.poll();
  }
 }

 public int add(int val) {
  if(minHeap.size()<k||val>minHeap.peek()) minHeap.add(val);
  if(minHeap.size()>k) minHeap.poll();
  return minHeap.peek();
 }
}
/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
