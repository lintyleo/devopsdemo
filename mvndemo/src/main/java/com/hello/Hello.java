package com.hello;

/**
 * 写一个类，实现list 获取最大的元素等
 */
class Hello {

    /**
     * 获取最大的元素
     *
     * @param aList 数组
     * @return int
     */
    int getMaxElement(int[] aList) {
        int maxValue = Integer.MIN_VALUE;
        for (int value : aList
        ) {
            if (maxValue < value) {
                maxValue = value;
            }
        }
        return maxValue;
    }

    int add(int a, int b) {
        return a + b;
    }


}

