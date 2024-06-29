<script>
  import "../app.pcss";
  import { page } from '$app/stores';
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  $: activeUrl = $page.url.pathname;
  import { DarkMode } from 'flowbite-svelte';
  import { Footer, FooterBrand, FooterCopyright, FooterIcon, FooterLink, FooterLinkGroup } from 'flowbite-svelte';
  import { onNavigate } from '$app/navigation';
  import { injectSpeedInsights } from '@vercel/speed-insights/sveltekit';
  import { inject } from '@vercel/analytics';    

  // injectSpeedInsights();

</script>

<Navbar class="bg-blue-700">
  <NavBrand href="/">
    <span class="self-center whitespace-nowrap text-xl font-semibold text-white">DroneWorks</span>
  </NavBrand>
  <!-- <NavHamburger/> -->
  <!-- <NavUl>
    <NavLi href="/" class="text-white">Home</NavLi>
  </NavUl> -->
</Navbar>

<slot></slot>