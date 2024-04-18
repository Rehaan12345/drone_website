import type { RequestHandler } from '@sveltejs/kit';

export const GET: RequestHandler = async () => {
	const fs = await import("fs");
	const dir = import.meta.env.PROD? fs.opendirSync('client/images'): fs.opendirSync('static/images');
	const images = [];
	for await (const dirent of dir) {
     images.push({title: dirent.name, src: `images/${dirent.name}`});
	}

	return new Response(JSON.stringify(images), {
		headers: { 'content-type': 'application/json' }
	});
};