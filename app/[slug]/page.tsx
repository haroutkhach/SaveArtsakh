import fs from "fs";
// import Markdown from "markdown-to-jsx";
// import matter from "gray-matter";
// import getPostMetadata from "@/components/getPostMetadata";
import Image from "next/image";

// change this so it takes articles from a file called newsarticles.json and 
// const getPostContent = (slug: string) => {
//   const folder = "posts/";
//   const file = `${folder}${slug}.md`;
//   try {
//     const content = fs.readFileSync(file, "utf8");
//     const matterResult = matter(content);
//     return matterResult;
//   } catch (err) {
//     const matterResult = null;
//     return matterResult;
//   }
// };

interface Article {
  source: {
    id: string | null;
    name: string;
  };
  author: string;
  title: string;
  description: string;
  url: string;
  urlToImage: string;
  publishedAt: string;
  content: string;
}

const getPostContent = (slug: string): Article | null => {
  const file = 'news_articles.json'; // Assuming the JSON file is in the same directory

  try {
    const jsonData = fs.readFileSync(file, 'utf8');
    const data = JSON.parse(jsonData);

    // Assuming articles is an array of objects with titles that can be used as slugs
    const article = data.articles.find((article: Article) => article.title === slug);
    
    if (article) {
      // You can return the article content here, or modify as needed
      return article;
    } else {
      // Handle the case where the article with the specified slug was not found
      return null;
    }
  } catch (err) {
    // Handle any errors, e.g., file not found, invalid JSON format, etc.
    console.error(err);
    return null;
  }
};

// export const generateStaticParams = async () => {
//   const posts = getPostMetadata();
//   return posts.map((post) => ({
//     slug: post.slug,
//   }));
// };

// function PostPage(props: any) {
//   const slug = props.params.slug;

//   const post = getPostContent(slug);
//   if (post == null) {
//     return (
//       <div className="py-5">
//         <h1 className="text-center mb-5 title">404: This Page Doesn't Exist</h1>
//         <article className="text-center article">
//           Go to homepage to find latest articles!
//         </article>
//       </div>
//     );
//   }
//   return (
//     <div className="mx-4 my-10">
//       <div className="my-2 text-center px-1 font-semibold  text-[#e53170] text-base md:text-lg tracking-wide">
//         <span className="flex justify-center">
//           {post.Article.url.map((url: string) => {
//             return (
//               <div key={url} className="pr-4">
//                 {url}
//               </div>
//             );
//           })}
//         </span>
//       </div>
//       <h1 className=" text-black text-center text-3xl md:text-4xl font-extrabold ">
//         {post.Article.title}
//         <p>AHGHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH</p>
//       </h1>
//       <div className="text-gray-600 text-base md:text-lg font-medium text-center my-3">
//         <span>{post.Article.subtitle}</span>
//       </div>
//       <article className="article">
//         <figure className="">
//           <Image
//             src={post.Article.featured_image}
//             alt=""
//             width={800}
//             height={480}
//             priority
//           />
//         </figure>
//         <div className="flex justify-center my-4 ">
//           <div className="font-medium text-gray-600 text-base md:text-lg tracking-wide">
//             By
//           </div>
//           <div className="px-1 font-semibold  text-[#e53170] text-base md:text-lg tracking-wide">
//             {post.Article.author}
//           </div>
//           <div className="font-medium text-base md:text-lg text-gray-600 tracking-wide">
//             & Published on {post.Article.date}
//           </div>
//         </div>
//         <div className="prose md:prose-xl">
//           <Markdown>{post!.content}</Markdown>
//         </div>
//       </article>
//     </div>
//   );
// }
import { Link } from 'react-router-dom'; // Import Link from React Router

function PostPage(props: any) {
  const slug = props.params.slug;

  const post = getPostContent(slug);
  if (post == null) {
    return (
      <div className="py-5">
        <h1 className="text-center mb-5 title">404: This Page Doesn't Exist</h1>
        <article className="text-center article">
          Go to the homepage to find the latest articles!
        </article>
      </div>
    );
  }
  return (
    <div className="mx-4 my-10">
      <h1 className="text-black text-center text-3xl md:text-4xl font-extrabold">
        {post.title}
      </h1>
      <article className="article">
        <figure className="">
          <Image
            src={post.urlToImage}
            alt=""
            width={800}
            height={480}
            priority
          />
        </figure>
        <div className="flex justify-center my-4">
          <div className="font-medium text-gray-600 text-base md:text-lg tracking-wide">
            By
          </div>
          <div className="px-1 font-semibold text-[#e53170] text-base md:text-lg tracking-wide">
            {post.author}
          </div>
          <div className="font-medium text-base md:text-lg text-gray-600 tracking-wide">
            & Published on {post.publishedAt}
          </div>

        </div>
        {/* Add a Link to navigate to a new page with the content */}
        <Link to={`/full-content/${slug}`} className="text-blue-500">
          Read Full Content
        </Link>
      </article>
    </div>
  );
}

export default PostPage;
