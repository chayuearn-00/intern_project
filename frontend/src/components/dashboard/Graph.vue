<template>
    <div class="bg-white rounded-2xl shadow w-full h-100 flex flex-col"> 
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
import { watch, ref, onMounted, onBeforeUnmount, nextTick } from 'vue';
import VChart from "vue-echarts";
import * as echarts from "echarts";

const props = defineProps({
  devices: Array, // [{ id, name }]
  initialRecords: Object, // { [deviceId]: [{ time, value }] }
  latestData: Object, // { [deviceId]: { time, value } }
  visibleDevices: Array, // [deviceId] (optional, for parent to control which lines to show)
});

const chartRef = ref(null);

const chartOption = ref({
  //แสดงข้อมูลที่เอาเมาส์ไปชี้
  tooltip: { trigger: "axis" },
  //ชื่อข้อมูลในกราฟ (จะมีการใส่ค่าข้อมูลตามหลังมาอีกที)
  legend: {},
  xAxis: {
    type: "category",
    data: [],
    // gap ซ้าย-ขวา
    boundaryGap: false,
  },
  yAxis: {
    type: "value",
    min: 0,
    max: 100,
  },
  // ชุดข้อมูล
  series: [],
  grid: {
    left: 20,
    right: 40,
    top: 20,
    bottom: 30,
    // ขยับกราฟอัตโนมัติ
    containLabel: true,
  },
});

const deviceData = ref({}); // { [deviceId]: [{ time, value }] }

const handleResize = () => {
  if (chartRef.value && chartRef.value.getEchartsInstance) {
    const instance = chartRef.value.getEchartsInstance();
    if (instance && instance.resize) instance.resize();
  }
};

function updateChart() {
  // Determine which devices to show
  const showDevices = props.visibleDevices && props.visibleDevices.length
    ? props.visibleDevices
    : props.devices.map(d => d.id);

  // Build xAxis from the first device's data (or union of all times)
  let allTimes = [];
  showDevices.forEach(id => {
    if (deviceData.value[id]) {
      allTimes = allTimes.concat(deviceData.value[id].map(d => d.time));
    }
  });
  // Unique and sorted times
  const xAxisData = Array.from(new Set(allTimes)).sort();
  chartOption.value.xAxis.data = xAxisData;

  // Build series for each device
  chartOption.value.series = showDevices.map((id, idx) => {
    const device = props.devices.find(d => d.id === id);
    return {
      name: device ? device.name : id,
      type: "line",
      smooth: true,
      data: xAxisData.map(time => {
        const point = (deviceData.value[id] || []).find(d => d.time === time);
        return point ? point.value : null;
      }),
      areaStyle: {},
    };
  });
  chartOption.value.legend = showDevices.map((id, idx) => {
    const device = props.devices.find(d => d.id === id);
    return {
      orient: 'vertical',
      bottom: 'bottom',
      data: ['Battery','Motor','Signal'],
    };
  });
}

function pushLatestData() {
  // For each device, push latestData if available
  Object.keys(props.latestData || {}).forEach(id => {
    if (!deviceData.value[id]) deviceData.value[id] = [];
    deviceData.value[id].push(props.latestData[id]);
    // Keep only last 20
    if (deviceData.value[id].length > 20) deviceData.value[id].shift();
  });
  updateChart();
}

// Watch for initialRecords changes
watch(
  () => props.initialRecords,
  (newRecords) => {
    if (newRecords) {
      deviceData.value = { ...newRecords };
      updateChart();
    }
  },
  { immediate: true }
);

// Watch for latestData changes
watch(
  () => props.latestData,
  (newLatest) => {
    if (newLatest) {
      pushLatestData();
    }
  }
);

// Watch for visibleDevices changes
watch(
  () => props.visibleDevices,
  () => {
    updateChart();
  }
);

onMounted(() => {
  nextTick(() => {
    setTimeout(() => {
      if (chartRef.value && chartRef.value.getEchartsInstance) {
        const instance = chartRef.value.getEchartsInstance();
        if (instance && instance.resize) instance.resize();
      }
    }, 100);
  });
  window.addEventListener("resize", handleResize);
});

onBeforeUnmount(() => {
  window.removeEventListener("resize", handleResize);
});
</script>