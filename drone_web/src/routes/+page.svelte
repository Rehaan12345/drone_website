<script>
  import { Heading, P, Button, Mark, Span } from 'flowbite-svelte';
  import { ArrowRightOutline } from 'flowbite-svelte-icons';
  import { Gallery } from 'flowbite-svelte';
  import { onMount } from "svelte";
  import { fade, blur, fly } from 'svelte/transition';
  import { quintOut } from 'svelte/easing';
  import { Carousel, Thumbnails } from 'flowbite-svelte';
  import { CldUploadWidget } from 'svelte-cloudinary';
  import { vimeo } from "vimeo";
  // import images from "/imageData/images.json";

  // import images from './imageData/images.json';

  let index = 0;
  let forward = true; // sync animation direction between Thumbnails and Carousel

  // import db from "../firebase"

  // Intersection Obvserver functionality: (source: https://www.youtube.com/watch?v=T33NN_pPeNI)
  let ready = false;
  onMount(() => {
    // console.log(db);

    ready = true;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          console.log(entry.target);
          entry.target.classList.add("show");
          entry.target.classList.remove("hiddensec");
        } else { 
          entry.target.classList.remove("show"); 
          entry.target.classList.add("hiddensec"); 
        }
      });
    });

    const hiddenElements = document.querySelectorAll(".hiddensec");
    hiddenElements.forEach((el) => observer.observe(el));
  });

  let Vimeo = require('vimeo').Vimeo;
  let client = new Vimeo("fb93e2b9ae86ab4b78ff357ab3c3bbf33121e389", "9no7IJ2dXvE3oiN1TwxecAqu+2gjXw75oFurkDPeu4xbT+XVDdDuOF4ijWfDeaX3QKbskzhNruGxsnvr9BZKdfVVTyyB/GtgGLOpoOqWOBwo1TgdSE/HXhxkxTgcUFrV", "ae62ce47d0ad85e2deb5ae81d9fcd11e");

  client.request({
    method: 'GET',
    path: '/'
  }, function (error, body, status_code, headers) {
    if (error) {
      console.log(error);
    }

    console.log(body);
  })

</script>

<style>

.sectionsok  {
  min-height: 100vh;
  color: white;
  display: grid;
  place-content: center;
}

.hiddensec {
  opacity: 0;
  filter: blur(5px);
  transform: translateX(-100%);
  transition: all 5s;
}

.show {
  opacity: 1;
  transform: translateX(0);
}

</style>

<div class="show"></div>

<!-- <div class="max-w-4xl space-y-4">
  <Carousel {images} {forward} let:Indicators let:Controls bind:index>
    <Controls />
    <Indicators />
  </Carousel>
  <Thumbnails {images} {forward} bind:index />
</div> -->

<!-- <enhanced:img src="../lib/images/Pic1.png" alt="firstpic" /> -->

{#if ready}

  <div class="hero min-h-screen">
    <div class="hero-overlay bg-opacity-30"></div>
    <div class="hero-content text-center text-neutral-content">
      <div class="max-w-md">
        <Heading tag="h1" class="mb-4">
          <Span underline decorationClass="decoration-8 decoration-orange-400 dark:decoration-orange-600"><div class="part partone" transition:fly={{ delay: 0, duration: 800, x: 0, y: -500, opacity: 0, easing: quintOut }}>Custom</div></Span> 
          <div class="part parttwo" transition:fly={{ delay: 500, duration: 800, x: -1000, y: 0, opacity: 0, easing: quintOut }}>drone footage for </div>
          <Span underline decorationClass="decoration-8 decoration-orange-400 dark:decoration-orange-600"><div class="part partthree" transition:fly={{ delay: 700, duration: 800, x: 1000, y: 0, opacity: 0, easing: quintOut }}>every project.</div></Span> 
        </Heading>
        <P><center transition:blur={{ delay: 900, duration: 600, amount: 10 }}>Beantown drones combines high-quality aerial photo and video with a customized portfolio for every client, tailor made to fit your goal.</center></P>
        <br>
        <div class="part partfour" transition:fly={{ delay: 1000, duration: 800, x: 0, y: 500, opacity: 0, easing: quintOut }}><Button href="/#section1">Explore</Button></div>
      </div>
    </div>
  </div>
{:else}
  <span class="loading loading-infinity loading-lg"></span>
{/if}

<section transition:blur={{ delay: 500, duration: 400, opacity: 0 }} class="sectionsok" id="section1">
  <Heading>Section 1</Heading>
</section>

<section class="sectionsok hiddensec" id="section2">
  <Heading>Section 2</Heading>
</section>