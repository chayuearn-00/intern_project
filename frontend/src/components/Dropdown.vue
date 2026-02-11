<template>
    <div class="grid grid-cols-3 gap-10 divide-x-2 divide-solid w-full p-7.5 rounded-xl bg-dropdown">
        <div class="text-black">
            <p class="text_dropbox">Main Pages</p>
            <a
                v-for="item in mainPages"
                :key="item.name"
                :href="item.link"
                class="link_dropbox"
            >
                {{ item.name }}
            </a>
        </div>
        <div>
            <p class="text_dropbox">Inner Pages</p>
            <a
                v-for="item in innerPages"
                :key="item.name"
                :href="item.link"
                class="link_dropbox"
            >
                {{ item.name }}
            </a>
        </div>
        <div>
            <p class="text_dropbox">Utility Pages</p>
            <a
                v-for="item in utilityPages"
                :key="item.name"
                :href="item.link"
                class="link_dropbox"
            >
                {{ item.name }}
            </a>
        </div>
    </div>
</template>

<script setup>
const mainPages = [
  { name: 'Home', link: '#' },
  { name: 'Features', link: '#' },
  { name: 'Blogs', link: '#' },
  { name: 'Pricing', link: '#' },
]

const innerPages = [
  { name: 'Prising Single', link: '#' },
  { name: 'Blog Single', link: '#' },
  { name: 'contact', link: '#' },
]

const utilityPages = [
  { name: 'Style Guide', link: '#' },
  { name: 'License', link: '#' },
  { name: 'Changelog', link: '#' },
  { name: 'Password Protected', link: '#' },
  { name: '404', link: '#' },
]
</script>