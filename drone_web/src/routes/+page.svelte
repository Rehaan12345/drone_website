<script>
  import { Heading, P, Button, Mark, Span, A } from 'flowbite-svelte';
  import { ArrowRightOutline, InstagramSolid } from 'flowbite-svelte-icons';
  import { Gallery } from 'flowbite-svelte';
  import { onMount } from "svelte";
  import { fade, blur, fly } from 'svelte/transition';
  import { quintOut } from 'svelte/easing';
  import { Carousel, Thumbnails } from 'flowbite-svelte';
  import { CldUploadWidget } from 'svelte-cloudinary';
  import { BadgeCheckOutline, EnvelopeSolid } from "flowbite-svelte-icons";
  import { Alert } from "flowbite-svelte";
  import { CldVideoPlayer } from 'svelte-cloudinary';
  import Contact from "./Contact.svelte";

  let msg;
  let password;

  async function testAPI() {
      try {
          const url = "https://droneweb-backend.vercel.app/data/";
          const res = await fetch(url);
          if (!res.ok) {
              throw new Error("API fetching didn't work");
          }
          const resData = await res.json();
          msg = resData["message"];
          console.log("Successfully retrieved message: " + msg);
      } catch (error) {
          console.log("Error retrieving login info: ", error);
      }
  }

  onMount(() => { testAPI(); });
 
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

  let vid;

  // async function getVid() {
  //     try {
  //         const url = "http://localhost:8000/getvid/";
  //         console.log("Fetching");
  //         const res = await fetch(url);
  //         console.log("Fetch complete");
  //         if (!res.ok) {
  //             throw new Error("Fetching didn't work");
  //         }
  //         const resData = await res.json();
  //         const vid = resData["vid"];
  //         console.log("Video: " + vid);
  //     } catch (error) {
  //         console.log("Error retrieving video: ", error);
  //     }
  // }

  // onMount(() => vid = getVid());

</script>

<style>

.sectionsok  {
  /* min-height: 90vh; */
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
}

.show {
  opacity: 1;
  transform: translateX(0);
}

.moreinfowrapper {
  margin-right: 5rem;
  margin-left: 5rem;
}

.buttons {
  margin-top: 5rem;
  margin-bottom: 5rem;
  /* border: 1px solid white; */
  /* padding: 5rem; */
  display: grid;
  gap: 2rem;
  justify-content: center;
  align-items: center;
}

</style>

<div class="show"></div>

{#if ready}

  <div class="hero min-h-screen bg-gray-900">
    <div class="hero-overlay bg-opacity-30"></div>
    <div class="hero-content text-center text-neutral-content">
      <div class="max-w-md">
        <Heading class="text-white">
          Making your
        </Heading>
        <Heading class="text-white">
          aerial dreams
        </Heading>
        <Heading class="text-white">
          come true!
        </Heading>
        <br>
        <!-- <div class="part partfour" transition:fly={{ delay: 1000, duration: 800, x: 0, y: 500, opacity: 0, easing: quintOut }}><Button href="/#section1" class="bg-blue-800">Explore</Button></div> -->
        <Button href="#section1" class="bg-blue-600">Explore</Button>
      </div>
    </div>
  </div>
  <section transition:blur={{ delay: 500, duration: 400, opacity: 0 }} class="sectionsok bg-gray-800" id="section1">
    <div class="moreinfowrapper">
      <br><br><br><br>
      <article class="format lg:format-lg">
        <center><h1 class="text-white">Who are we?</h1></center>
        <p class="lead text-white">
          We are a team of aerial photographers with a combined 10 years of drone-piloting experience, breaking into the world of commercial filming. 
        </p>
        <p class="text-white">
          FAA certified and insured, with the Part 107 license, we film, edit, and publish high quality, custom projects for every customer.
        </p>
        <enhanced:img src="../lib/images/droneworksfounders.jpg" alt="Founders">
       </article>
       <br><br>
       <article class="format lg:format-lg">
        <center><h1 class="text-white">Media</h1></center>
        <p class="lead text-white">
          We have over 200 hours of collective footage, ranging from beautiful scenery of the Charles River, down to professional-grade real estate photography. All shot by drones!
        </p>
        <enhanced:img src="../lib/images/goodweddingpic.jpg" alt="Wedding"></enhanced:img>
       </article>
       <br><br>
       <article class="format lg:format-lg">
        <center><h1 class="text-white">Packages</h1></center>
        <p class="lead text-white">
          Our packages start at $200 for two hours of work, not including the additional costs for any venue more than 40 miles outside of Boston.
        </p>
        <p class="text-white">
          <a href="mailto:droneworks@bosdroneworks.com" class="text-white">Email</a> us for any questions you have!
        </p>
        <p class="text-white">
        </p>
        <enhanced:img src="../lib/images/italypic.jpg" alt="Italy"></enhanced:img>
       </article>
    </div>
  </section>
  
  <section class="sectionsok bg-gray-800" id="section3">
    <div class="buttons">
      <Button size="xl" target="_blank" class="bg-blue-700"><EnvelopeSolid class="w-6 h-6 me-2"/><a href="mailto:droneworks@bosdroneworks.com">Send us an email!</a></Button>
      <Button size="xl" target="_blank" class="bg-purple-600"><InstagramSolid></InstagramSolid><a href="https://www.instagram.com/droneworks.media/">Follow our Instagram!</a></Button>
    </div>
  </section>
  
  
  <Alert color="yellow" bordercolor="blue">
    <span><b>Website Under Construction:</b></span>
    We are still developing the site, so let us know of any suggestions, and stay tuned for future improvements!
  </Alert>

{:else}

  <div class="spinnercontainer bg-gray-200">
    <span class="spinner loading loading-infinity loading-lg"></span>
  </div>

{/if}

