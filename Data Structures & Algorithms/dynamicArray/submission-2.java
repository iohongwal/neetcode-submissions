class DynamicArray {
    
    private int capacity = 0;
    private int length = 0;
    private int[]arr;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.length = 0;
        this.arr = new int[this.capacity];
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if(length == capacity){
            resize();
        }
        arr[length] = n;
        length++;
    }

    public int popback() {
        length --;
        return arr[length];
    }

    private void resize() {
        capacity *=2;
        int[] newArr = new int[capacity];
        for(int i = 0; i < length; i++){
            newArr[i] = arr[i]; 
        }
        arr = newArr;
    }

    public int getSize() {
        return length;
    }

    public int getCapacity() {
        return capacity;
    }
}
