<script>
  import { Heading, P, Button, Mark, Span } from 'flowbite-svelte';
  import { ArrowRightOutline } from 'flowbite-svelte-icons';
  import { Gallery } from 'flowbite-svelte';
  import { onMount } from "svelte";
  import { fade, blur, fly } from 'svelte/transition';
  import { quintOut } from 'svelte/easing';
  import { Carousel, Thumbnails } from 'flowbite-svelte';
  import { CldUploadWidget } from 'svelte-cloudinary';
  import { BadgeCheckOutline, EnvelopeSolid } from "flowbite-svelte-icons";
  import Contact from "./Contact.svelte";
 
  // import { vimeo } from "vimeo";
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

  // let Vimeo = require('vimeo').Vimeo;
  // let client = new Vimeo("fb93e2b9ae86ab4b78ff357ab3c3bbf33121e389", "9no7IJ2dXvE3oiN1TwxecAqu+2gjXw75oFurkDPeu4xbT+XVDdDuOF4ijWfDeaX3QKbskzhNruGxsnvr9BZKdfVVTyyB/GtgGLOpoOqWOBwo1TgdSE/HXhxkxTgcUFrV", "ae62ce47d0ad85e2deb5ae81d9fcd11e");

  // client.request({
  //   method: 'GET',
  //   path: '/'
  // }, function (error, body, status_code, headers) {
  //   if (error) {
  //     console.log(error);
  //   }

  //   console.log(body);
  // })

</script>

<style>

.sectionsok  {
  min-height: 90vh;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
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

.sectioncontent {
  display: flex;
  justify-content: center;
  align-items: center;
}

.sectionheadingwrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 10rem;
  margin-left: 10rem;
}

.sectioninfotext {
  margin-right: 20rem;
  display: flex;
}

</style>

<div class="show"></div>

{#if ready}

  <div class="hero min-h-screen">
    <div class="hero-overlay bg-opacity-30"></div>
    <div class="hero-content text-center text-neutral-content">
      <div class="max-w-md">
        <Heading>
          Making your
        </Heading>
        <Heading>
          aerial dreams
        </Heading>
        <Heading>
          come true!
        </Heading>
        <!-- <Heading tag="h1" class="mb-4">
          <Span underline decorationClass="decoration-8 decoration-orange-400 dark:decoration-orange-600"><div class="part partone" transition:fly={{ delay: 0, duration: 800, x: 0, y: -500, opacity: 0, easing: quintOut }}>Custom</div></Span> 
          <div class="part parttwo" transition:fly={{ delay: 500, duration: 800, x: -1000, y: 0, opacity: 0, easing: quintOut }}>drone footage for </div>
          <Span underline decorationClass="decoration-8 decoration-orange-400 dark:decoration-orange-600"><div class="part partthree" transition:fly={{ delay: 700, duration: 800, x: 1000, y: 0, opacity: 0, easing: quintOut }}>every project.</div></Span> 
        </Heading>
        <P><center transition:blur={{ delay: 900, duration: 600, amount: 10 }}>Beantown drones combines high-quality aerial photo and video with a customized portfolio for every client, tailor made to fit your goal.</center></P> -->
        <br>
        <div class="part partfour" transition:fly={{ delay: 1000, duration: 800, x: 0, y: 500, opacity: 0, easing: quintOut }}><Button href="/#section1">Explore</Button></div>
      </div>
    </div>
  </div>
{:else}
  <span class="loading loading-infinity loading-lg"></span>
{/if}

<section transition:blur={{ delay: 500, duration: 400, opacity: 0 }} class="sectionsok" id="section1">
  <div class="sectioncontent">
    <div class="sectionheadingwrapper">
      <Heading>Who are we?</Heading>
    </div>
    <!-- Add picture of both of us here below: -->
     <div class="sectioninfowrapper" id="section1info">
      <p class="sectioninfotext">
        <BadgeCheckOutline></BadgeCheckOutline> We are a team of aerial photographers with a combined 10 years of drone-piloting experience, breaking into the world of commercial filming. FAA certified and insured, with the Part 107 license, we film, edit, and publish high quality, custom projects for every customer.
      </p>
      <p class="sectioninfotext">
        <BadgeCheckOutline></BadgeCheckOutline> We work with care, integrity, and passion, ensuring everything we deliver to our clients represents the best that we can offer, and then some.
      </p>
     </div>
  </div>
</section>

<section class="sectionsok hiddensec" id="section2">
  <div class="sectioncontent">
    <div class="sectionheadingwrapper">
      <Heading>Media</Heading>
    </div>
    <div class="sectioninfowrapper" id="section2info">
      <p class="sectioninfotext">
        <BadgeCheckOutline class="checkmark">OKK</BadgeCheckOutline> Scroll through our media! We have over 200 hours of collective footage, ranging from beautiful scenery of the Charles River, down to professional-grade real estate photography. All shot by drones!
      </p>
    </div>
  </div>
</section>

<section class="sectionsok" id="section3">
  <div class="sectioncontent">
    <Button size="xl"><EnvelopeSolid class="w-6 h-6 me-2" />Send us an email!</Button>
  </div>
</section>