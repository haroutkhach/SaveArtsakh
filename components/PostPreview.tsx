import Link from "next/link";
import { Article } from "./PostMetadata";
import Image from "next/image";

const PostPreview = (article: Article) => {
  console.log(article.urlToImage);
  
  return (
    <div className="p-4 transition duration-200 transform hover:translate-y-2">
      <div className="hover:opacity-80">
        <Link href={`/${article.url}`}>
          {article.urlToImage && ( // Conditional rendering for the image
            <Image src={article.urlToImage} alt="" width="800" height="400" />
          )}
          <h4 className="font-bold text-lg pt-2 tracking-wide">
            {article.title}
          </h4>
        </Link>
      </div>
      <div className="flex">
        <p className="text-sm pt-3 tracking-wider font-medium pr-1">By</p>
        <p className="text-sm pt-3 text-[#e53170] tracking-wider font-semibold">
          {article.author}
        </p>
      </div>
      <p className="text-sm pt-3 text-gray-600 tracking-wider">
        {article.title}
      </p>
    </div>
  );
};

export default PostPreview;