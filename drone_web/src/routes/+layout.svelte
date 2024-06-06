<script>
  import "../app.pcss";
  import { page } from '$app/stores';
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  $: activeUrl = $page.url.pathname;
  import { DarkMode } from 'flowbite-svelte';
  import { Footer, FooterBrand, FooterCopyright, FooterIcon, FooterLink, FooterLinkGroup } from 'flowbite-svelte';

  import { onNavigate } from '$app/navigation';

  // onNavigate((navigation) => {
  //   if (!document.startViewTransition) return;

  //   return new Promise((resolve) => {
  //     document.startViewTransition(async () => {
  //       resolve();
  //       await navigation.complete;
  //     });
  //   });
  // });

</script>

<Navbar let:NavContainer color="primary">
    <NavBrand href="/">
      <DarkMode />
      <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Drone Works</span>
    </NavBrand>
    <NavHamburger />
    <NavUl {activeUrl}>
      <NavLi href="/">Home</NavLi>
      <NavLi href="/Pricing">Pricing</NavLi>
      <NavLi href="/Purchase">Purchase</NavLi>
      <NavLi href="/Signup">Sign Up</NavLi>
    </NavUl>
  </Navbar>

<slot></slot>