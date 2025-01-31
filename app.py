import streamlit as st

def main():
    # Define your HTML content
    html_content = """
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100">
    <div class="container   min-h-screen px-6 py-3 ">

        <nav class="flex items-center gap-4 px-10 py-4">
            <img src="book.png" alt="" class="w-14 h-14">
            <p class="font-bold text-2xl">DSA Revision</p>
        </nav>

        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 xl:grid-cols-2 gap-4 leading-normal  ">
            <div class="mt-12 ml-12 flex flex-col justify-center place-items-baseline order-2 sm:order-1 md:order-1 xl:order-1">
                <h1 class="font-bold text-6xl ">Best way to revise for your next coding interview</h1>
                <p class="mt-4">Get everything in a single guide . Data structures , algorithms , patterns
                    ,visuliazers
                    , questions ,examples , solutions ,explainations , and much more.</p>

                <button
                    class= " text-white bg-black hover:bg-pink-500 hover:text-black px-3 py-2 rounded-lg w-full mt-4">Buy
                    FREE through <p class="inline-block text-green-500 hover:text-indigo-700">WEBSITE</p></button>

                    

                    

            </div>
            <div class="flex mt-12 justify-center items-center order-1 sm:order-2 md:order-2 xl:order-2">
                <img src="./certificate.png" alt="" class="h-screen">
            </div>


        </div>

    </div>
    <h1 class="text-center font-bold text-4xl mt-6">What's included</h1>
    <div class="container mx-auto">


        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2  xl:grid-cols-2 gap-12 justify-center  mr-10 ">

            <div class="mt-10 ml-12 flex justify-center items-center">
                <img src="./certificate.png" alt="" class="w-72 ">

            </div>
            <div class="flex flex-col mt-12 sm:mt-6 md:mt-6 xl:mt-6 justify-between ml-10 mr-8 place-items-baseline ">
                <div class="flex mb-2 gap-2">
                    <img src="./check.png" alt="" class="w-6 h-6">
                    <p>15+ algo patterns Discussed</p>
                </div>
                <div class="flex mb-2 gap-2">
                    <img src="./check.png" alt="" class="w-6 h-6">
                    <p>Detailed solutions and explainations</p>
                </div>
                <div class="flex mb-2 gap-2">
                    <img src="./check.png" alt="" class="w-6 h-6">
                    <p>Awesome resources, articles, blogs</p>
                </div>
                <div class="flex mb-2 gap-2">
                    <img src=".check.png" alt="" class="w-6 h-6">
                    <p>Visulizers and animations included</p>
                </div>
                <div class="flex mb-2 gap-2">
                    <img src=".check.png" alt="" class="w-6 h-6">
                    <p>100 pages of quality content </p>
                </div>
                <div class="flex mb-2 gap-2">
                    <img src="./check.png" alt="" class="w-6 h-6">
                    <p>Concepts explains for beginners</p>
                </div>
                <button class="bg-orange-500 text-white rounded-full ml-12 px-3 py-2 hover:bg-orange-600">Download for
                    FREE</button>
            </div>

        </div>
    </div>


    <section class="testimonials grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 xl:grid-cols-2 p-12 gap-6  text-gray-600 mt-6">
		<div class="testiCard border p-4">
			<p class="desc">
				“Walling helps us <strong>visually organise ideas and tasks</strong>,
				work collaboratively and efficiently within our team. The visual
				experience makes it so easy to plan content and stay on track with our
				projects and campaigns.”
			</p>
			<div class="author flex mt-4 gap-4">
				<img src="./my_img.jpg" alt="" class="w-12 h-12 rounded-full"/>
				<div class="authorCol">
					<p class="text-blue-700">Rahul Singh Dani</p>
					<p>Head of Development</p>
				</div>
			</div>
		</div>
		<div class="testiCard p-4 border">
			<p class="desc">
				“Walling helps us <strong>visually organise ideas and tasks</strong>,
				work collaboratively and efficiently within our team. The visual
				experience makes it so easy to plan content and stay on track with our
				projects and campaigns.”
			</p>
			<div class="author flex mt-4 gap-4">
				<img src="./my_img.jpg" alt="" class="w-12 h-12 rounded-full" />
				<div class="authorCol">
					<p class="text-blue-700">Rahul Singh Dani</p>
					<p>Head of Development</p>
				</div>
			</div>
		</div>
		<div class="testiCard p-4 border">
			<p class="desc">
				“Walling helps us <strong>visually organise ideas and tasks</strong>,
				work collaboratively and efficiently within our team. The visual
				experience makes it so easy to plan content and stay on track with our
				projects and campaigns.”
			</p>
			<div class="author flex mt-4 gap-4">
				<img src="./my_img.jpg" alt="" class="w-12 h-12 rounded-full"/>
				<div class="authorCol">
					<p class="text-blue-700">Rahul Singh Dani</p>
					<p>Head of Development</p>
				</div>
			</div>
		</div>
		<div class="testiCard p-4 border">
			<p class="desc">
				“Walling helps us <strong>visually organise ideas and tasks</strong>,
				work collaboratively and efficiently within our team. The visual
				experience makes it so easy to plan content and stay on track with our
				projects and campaigns.”
			</p>
			<div class="author flex mt-4 gap-4">
				<img src="./my_img.jpg" alt="" class="w-12 h-12 rounded-full"/>
				<div class="authorCol">
					<p class="text-blue-700">Rahul Singh Dani</p>
					<p>Head of Development</p>
				</div>
			</div>
		</div>
	</section>

    <hr class=" mt-8 mb-4">

    <footer class="px-12 py-10 bg-gray-300 ">
        <h1 class="text-center"> "Master algorithms, unleash your potential. Dive deeper into DSA with our comprehensive
            resources and practice
            materials. <br> © 2024 DSARevision.com. All rights reserved ( Rahul Singh Dani)."</h1>
        <div class="container mx-auto">
            <div
                class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-3 gap-8 mt-10 px-12 py-4 bg-gray-200 ">


                <div class=" justify-start ">
                    <h1 class="text-3xl font-bold leading-normal">Solutions</h1>
                    <ul class="list-none inline-block ">
                        <li><a href="#">Marketing</a></li>
                        <li><a href="#">Analytics</a></li>
                        <li><a href="#">Algorithms</a></li>
                        <li><a href="#">Patterns</a></li>
                        <li><a href="#">Insides</a></li>
                    </ul>
                </div>
                <div class="">
                    <h1 class="text-3xl font-bold leading-normal">Support</h1>
                    <ul>
                        <li><a href="#">Pricing</a></li>
                        <li><a href="#">Documentation</a></li>
                        <li><a href="#">Guides</a></li>
                        <li><a href="#">Contact Us</a></li>
                        <li><a href="#">API Status</a></li>
                    </ul>
                </div>
                <div>
                    <h1 class="flex-1 text-3xl font-bold leading-normal">Company</h1>
                    <ul>
                        <li><a href="#">About</a></li>
                        <li><a href="#">Blog</a></li>
                        <li><a href="#">Jobs</a></li>
                        <li><a href="#">Press</a></li>
                        <li><a href="#">Parteners</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>

</body>

</html>
"""

    # Display the HTML content using Streamlit's `st.components.v1.html` function
    st.markdown(html_content, unsafe_allow_html=True)
	

if __name__ == "__main__":
    main()
