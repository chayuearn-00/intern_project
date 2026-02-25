<template>
    <div class="bg-white rounded-2xl shadow h-[250px] flex flex-col"> 
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
    device: String,
    value: Number
});

const data = ref([]);
const currentValue = ref(props.value || 50);
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
      name: props.device,
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
  // Wait for DOM to be fully laid out and painted
  nextTick(() => {
    setTimeout(() => {
      if (chartRef.value) {
        chartRef.value.resize();
      }
    }, 500);
  });

  watch(
    () => props.value,
    (newVal) => {
      if (newVal !== undefined) {
        updateChart(newVal);
      }
    }
  );

  function updateChart(value) {
    const time = new Date().toLocaleTimeString();

    data.value.push({
      time,
      value
    });

    if (data.value.length > 20) {
      data.value.shift();
    }

    chartOption.value.xAxis.data = data.value.map(d => d.time);
    chartOption.value.series[0].data = data.value.map(d => d.value);
  }

  window.addEventListener("resize", handleResize);

  onBeforeUnmount(() => {
    clearInterval(interval);
    window.removeEventListener("resize", handleResize);
  });
});
</script>