import fs from "fs";
import { Article } from "./PostMetadata";

const getPostMetadata = (): Article[] => {
  try {
    // Read the 'newsArticles.json' file
    const jsonData = fs.readFileSync('app/news/newsArticles.json', 'utf8');
     
    // Parse the JSON data
    const data = JSON.parse(jsonData);
    // Access the 'articles' array from the JSON data
    // Map the data to match the Article interface and return an array of articles
    const articleData: Article[] = data.map((article: any) => {
      return {
        source: {
          id: null,
          name: article.source.name,
        },
        author: article.author,
        title: article.title,
        description: article.description,
        url: article.url,
        urlToImage: article.urlToImage,
        publishedAt: article.publishedAt,
        content: article.content,
      };
    });

    return articleData;
  } catch (error) {
    console.error("Error reading or parsing 'newsArticles.json':", error);
    return [];
  }
};

export default getPostMetadata;


// import fs from "fs";
// import matter from "gray-matter";
// import { Article } from "./PostMetadata";

// const getPostMetadata = (): Article[] => {
//   // const folder = "posts/";
//   // const files = fs.readdirSync(folder);
//   // const markdownPosts = files.filter((file) => file.endsWith(".md"));

//   // //Get gray matter data from each file
//   // const posts = markdownPosts.map((fileName) => {
//   //   const fileContents = fs.readFileSync(`posts/${fileName}`, "utf8");
//   //   const articles = matter(fileContents);
//   const jsonData = fs.readFileSync('newsArticles.json', 'utf8');
//   const data = JSON.parse(jsonData);
//   const articles = data.articles;
//     return {
//       source: {
//         id: null, // You can set this to null or assign an appropriate value
//         name: articles.name,
//       },
//       author: articles.author,
//       title: articles.title,
//       description: articles.subtitle, // Assuming subtitle maps to description
//       url: articles.url,
//       urlToImage: articles.featured_image, // Assuming featured_image maps to urlToImage
//       publishedAt: articles.date, // Assuming date maps to publishedAt
//       content: '', // You can assign content based on your data structure
//     };
//     };
//   return posts;
// };


// export default getPostMetadata;
