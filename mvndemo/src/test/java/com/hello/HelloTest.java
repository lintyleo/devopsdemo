package com.hello;



import io.qameta.allure.Description;
import io.qameta.allure.Feature;
import io.qameta.allure.Severity;
import io.qameta.allure.SeverityLevel;
import org.junit.jupiter.api.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

    class HelloTest {
        private Hello hw = null;

        @BeforeEach
        void prepare() {
            this.hw = new Hello();
            System.out.println("每一个开始前，我都来了");
        }

        @AfterEach
        void clean() {
            System.out.println("每一个结束之后，我也来了");
        }

        @BeforeAll
        static void start() {
            System.out.println("在所有的都未开始之前，我先来");
        }

        @AfterAll
        static void end() {
            System.out.println("在所有的都结束后，我最后走");
        }

        @Test
        void testGetMaxElement01() {
            System.out.println("我是第一个测试 testGetMaxElement01");
            int[] listToTest = {12, 6, 9, 88, 46, 3};
            int expected = 88;
            int actual = this.hw.getMaxElement(listToTest);
            assertEquals(expected, actual, "有效的数据检查获取最大值");

        }

        @Test
        @DisplayName("第二个测试")
        void testGetMaxElement02() {

            System.out.println("我是第二个测试 testGetMaxElement02");

            int[] listToTest = {-12, -6, -9, -88, -46, -3};
            int expected = -3;
            int actual = this.hw.getMaxElement(listToTest);
            assertEquals(expected, actual, "有效的数据检查获取最大值");

        }

        @ParameterizedTest
        @CsvFileSource(resources = "/HelloTest.csv", numLinesToSkip = 1)
        @Description("描述描述")
        @Feature("特性aa")
        @Severity(SeverityLevel.CRITICAL)
        void testAdd(int a, int b, int e){
            int actual = this.hw.add(a, b);
            assertEquals(e, actual, "有效数据检查加法");
        }
    }
