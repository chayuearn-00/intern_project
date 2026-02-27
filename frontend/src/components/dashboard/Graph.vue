<template>
    <div class="bg-white rounded-2xl shadow max-w-full h-[250px] flex flex-col"> 
      <div class="flex-1">
        <v-chart
          ref="chartRef"
          class="w-full h-full"
          :option="chartOption"
        />
      </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, nextTick, watch } from "vue";
import VChart from "vue-echarts";
import * as echarts from "echarts";

const props = defineProps ({
    device1: String,
    value1: Number,
    device2: String,
    value2: Number,
});

const data1 = ref([]);
const data2 = ref([]);
const chartRef = ref(null);
let interval;

const handleResize = () => {
  chartRef.value?.resize();
};

const chartOption = ref({
  tooltip: { trigger: "axis" },
  xAxis: {
    type: "category",
    data: [],
    boundaryGap: false,
  },
  yAxis: {
    type: "value",
    min: 0,
    max: 100,
  },
  series: [
    {
      name: props.device1,
      type: "line",
      smooth: true,
      data: [],
      areaStyle: {}, // ทำให้มีพื้นหลังใต้เส้น
    },
    {
      name: props.device2,
      type: "line",
      smooth: true,
      data: [],
      areaStyle: {}, // ทำให้มีพื้นหลังใต้เส้น
    },
  ],
  grid: {
    left: 20,
    right: 40,
    top: 20,
    bottom: 20,
    containLabel: true
  },
});

onMounted(() => {
  // ensure chart resizes once the DOM is ready
  nextTick(() => {
    setTimeout(() => {
      if (chartRef.value) {
        chartRef.value.resize();
      }
    }, 100);
  });

  watch(
    () => [props.value1, props.value2],
    ([newVal1, newVal2]) => {
      if (newVal1 !== undefined) {
        updateChart(newVal1, newVal2);
      }
    }
  );

  function updateChart(val1, val2) {
    const time = new Date().toLocaleTimeString();

    data1.value.push({
      time,
      value: val1
    });

    data2.value.push({
      time,
      value: val2
    });

    if (data1.value.length > 20) {
      data1.value.shift();
    }

    if (val2 !== undefined) {
    data2.value.push({ time, value: val2 });
    if (data2.value.length > 20) data2.value.shift();
  }

  chartOption.value.xAxis.data = data1.value.map(d => d.time);

  chartOption.value.series[0].data = data1.value.map(d => d.value);
  // chartOption.value.series[1].data = data2.value.map(d => d.value);
  chartOption.value.series[1].data =
  val2 !== undefined
    ? data2.value.map(d => d.value)
    : [];
  }

  window.addEventListener("resize", handleResize);

  onBeforeUnmount(() => {
    clearInterval(interval);
    window.removeEventListener("resize", handleResize);
  });
});
</script>