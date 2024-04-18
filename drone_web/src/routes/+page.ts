import type { PageLoad } from './$types';

export const load: PageLoad = ({ fetch }) => {
	return {
		images: fetch('/images').then((r) => r.json())
	};
};
