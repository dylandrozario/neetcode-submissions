class DynamicArray {

    private int capacity;
    private int [] array;
    private int len;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.len = 0;
        this.array =  new int[capacity];

    }

    public int get(int i) {
        return array[i];
    }

    public void set(int i, int n) {
        array[i] = n;
    }

    public void pushback(int n) {
        if(capacity == len){
            resize();
        }
        array[len] = n;
        len++;
    }

    public int popback() {
        if (len > 0){
            len--;
        }
        return array[len];
    }

    private void resize() {
        capacity *= 2;
        int[] temp = new int[capacity];
        for(int i = 0; i < len; i++){
            temp[i] = array[i];
        }
        array = temp;
    }

    public int getSize() {
        return len;
    }

    public int getCapacity() {
        return capacity;
    }
}
