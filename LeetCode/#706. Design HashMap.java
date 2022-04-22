

class MyHashMap {

        int[] map;

        //Initialization of the hashmap
        public MyHashMap()  {
            map = new int[1000001];
            //fill the array as -1
            Arrays.fill(map,-1);
        }
        
        //Given the index "key" we put the value at the index of the map array
        public void put(int key, int value) {
            map[key] = value;
        }

        //Return the value at that particular index. If the key is empty we will return -1.(filled the array with -1 at the beginning)
        
        public int get(int key) {
            return map[key];
        }
        //To remove an key,simply put -1 at that index
        public void remove(int key) {
            map[key] = -1;
        }

}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */


/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
