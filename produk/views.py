from django.shortcuts import render

PRODUCTS = [
    {
        'id': 1,
        'name': 'Elegance Sofa',
        'category': 'Living Room',
        'sub': 'Sofa',
        'tagline': 'Timeless form, enduring comfort',
        'price': 'Rp 12.500.000',
        'image': 'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=600&q=80',
        'images': [
            'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=800&q=80',
            'https://images.unsplash.com/photo-1493663284031-b7e3aefcae8e?w=800&q=80',
            'https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?w=800&q=80',
        ],
        'specs': [
            ('Dimensions', '220 × 90 × 75 cm'),
            ('Material', 'Solid Teak & Linen'),
            ('Weight', '38 kg'),
            ('Availability', 'In Stock'),
        ],
        'desc': 'Crafted with precision and an eye for lasting elegance, this sofa brings warmth and structure to any living space. The solid teak frame provides durability while the linen upholstery is hand-finished for a supple, inviting feel.',
    },
    {
        'id': 2,
        'name': 'Natural Chair',
        'category': 'Accent',
        'sub': 'Chair',
        'tagline': 'Where nature meets refined craft',
        'price': 'Rp 4.800.000',
        'image': 'https://images.unsplash.com/photo-1538688525198-9b88f6f53126?w=600&q=80',
        'images': [
            'https://images.unsplash.com/photo-1538688525198-9b88f6f53126?w=800&q=80',
            'https://images.unsplash.com/photo-1506439773649-6e0eb8cfb237?w=800&q=80',
            'https://images.unsplash.com/photo-1561677978-583a8c7a4b43?w=800&q=80',
        ],
        'specs': [
            ('Dimensions', '60 × 62 × 82 cm'),
            ('Material', 'Rattan & Foam'),
            ('Weight', '6 kg'),
            ('Availability', 'In Stock'),
        ],
        'desc': 'A celebration of organic texture and honest materials. The rattan weave provides natural ventilation while the cushioned seat invites long, comfortable stays. Works beautifully as a reading corner piece or accent to any room.',
    },
    {
        'id': 3,
        'name': 'Serene Bed Frame',
        'category': 'Bedroom',
        'sub': 'Bed Frame',
        'tagline': 'Rest, restored to its purest form',
        'price': 'Rp 18.200.000',
        'image': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=600&q=80',
        'images': [
            'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=800&q=80',
            'https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=800&q=80',
            'https://images.unsplash.com/photo-1540518614846-7eded433c457?w=800&q=80',
        ],
        'specs': [
            ('Dimensions', '160 × 200 cm (Queen)'),
            ('Material', 'White Oak & Walnut'),
            ('Weight', '52 kg'),
            ('Availability', 'In Stock'),
        ],
        'desc': 'A sanctuary for sleep. The low-profile silhouette creates a sense of calm, while the white oak headboard adds subtle warmth. Engineered with dovetail joinery for a frame that will outlast trends and generations.',
    },
    {
        'id': 4,
        'name': 'Nordic Table',
        'category': 'Dining',
        'sub': 'Dining Table',
        'tagline': 'Gather around what matters',
        'price': 'Rp 9.100.000',
        'image': 'https://images.unsplash.com/photo-1611269154421-4e27233ac5c7?w=600&q=80',
        'images': [
            'https://images.unsplash.com/photo-1611269154421-4e27233ac5c7?w=800&q=80',
            'https://images.unsplash.com/photo-1577140917170-285929fb55b7?w=800&q=80',
            'https://images.unsplash.com/photo-1615571022219-eb45cf7faa9d?w=800&q=80',
        ],
        'specs': [
            ('Dimensions', '180 × 90 × 76 cm'),
            ('Material', 'Solid Ash Wood'),
            ('Weight', '44 kg'),
            ('Availability', 'In Stock'),
        ],
        'desc': 'Rooted in Scandinavian simplicity, this dining table strips away the unnecessary and celebrates honest wood grain. The tapered legs provide structural integrity while keeping the aesthetic light and airy.',
    },
    {
        'id': 5,
        'name': 'Shelf Modular',
        'category': 'Storage',
        'sub': 'Bookshelf',
        'tagline': 'Order, beautifully arranged',
        'price': 'Rp 6.750.000',
        'image': 'https://images.unsplash.com/photo-1595428774223-ef52624120d2?w=600&q=80',
        'images': [
            'https://images.unsplash.com/photo-1595428774223-ef52624120d2?w=800&q=80',
            'https://images.unsplash.com/photo-1544457070-4cd773b4d71e?w=800&q=80',
            'https://images.unsplash.com/photo-1519710164239-da123dc03ef4?w=800&q=80',
        ],
        'specs': [
            ('Dimensions', '80 × 30 × 180 cm'),
            ('Material', 'Plywood & Steel'),
            ('Weight', '22 kg'),
            ('Availability', 'In Stock'),
        ],
        'desc': 'A modular shelving system that adapts to your life. Display books, plants, ceramics, or all three. The open frame design keeps spaces feeling breathable, while the steel accents add an industrial warmth.',
    },
    {
        'id': 6,
        'name': 'Zen Coffee Table',
        'category': 'Living Room',
        'sub': 'Coffee Table',
        'tagline': 'Low and slow, by design',
        'price': 'Rp 3.200.000',
        'image': 'https://images.unsplash.com/photo-1518455027359-f3f8164ba6bd?w=600&q=80',
        'images': [
            'https://images.unsplash.com/photo-1518455027359-f3f8164ba6bd?w=800&q=80',
            'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=800&q=80',
            'https://images.unsplash.com/photo-1493663284031-b7e3aefcae8e?w=800&q=80',
        ],
        'specs': [
            ('Dimensions', '110 × 60 × 38 cm'),
            ('Material', 'Solid Walnut'),
            ('Weight', '14 kg'),
            ('Availability', 'In Stock'),
        ],
        'desc': 'Inspired by Japanese wabi-sabi philosophy, this coffee table celebrates the beauty of natural imperfection. Each piece features a unique grain pattern, making every table a one-of-a-kind object. Low-profile design keeps sightlines open.',
    },
    {
        'id': 7,
        'name': 'Loft Wardrobe',
        'category': 'Bedroom',
        'sub': 'Wardrobe',
        'tagline': 'Your wardrobe, curated',
        'price': 'Rp 22.400.000',
        'image': 'https://images.unsplash.com/photo-1551298370-9d3d53740c72?w=600&q=80',
        'images': [
            'https://images.unsplash.com/photo-1551298370-9d3d53740c72?w=800&q=80',
            'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=800&q=80',
            'https://images.unsplash.com/photo-1595526114035-0d45ed16cfad?w=800&q=80',
        ],
        'specs': [
            ('Dimensions', '180 × 60 × 220 cm'),
            ('Material', 'MDF & Soft-close Rail'),
            ('Weight', '78 kg'),
            ('Availability', 'Pre-order'),
        ],
        'desc': 'A wardrobe that does the heavy lifting. Thoughtful internal organisation with adjustable shelves, a full-length hanging rail, and integrated soft-close drawers. The clean exterior hides a world of considered detail within.',
    },
    {
        'id': 8,
        'name': 'Studio Desk',
        'category': 'Workspace',
        'sub': 'Desk',
        'tagline': 'Where ideas take shape',
        'price': 'Rp 7.900.000',
        'image': 'https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=600&q=80',
        'images': [
            'https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=800&q=80',
            'https://images.unsplash.com/photo-1517705008128-361805f42e86?w=800&q=80',
            'https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=800&q=80',
        ],
        'specs': [
            ('Dimensions', '140 × 70 × 75 cm'),
            ('Material', 'Bamboo & Powder-coated Steel'),
            ('Weight', '19 kg'),
            ('Availability', 'In Stock'),
        ],
        'desc': 'Designed for focus. The bamboo surface is naturally antibacterial and easy to maintain, while the steel legs provide solid stability even on uneven floors. A cable management groove runs the full length of the back edge.',
    },
]


def home(request):
    featured = PRODUCTS[:4]
    return render(request, 'produk/home.html', {'featured': featured})


def daftar_produk(request):
    return render(request, 'produk/daftar_produk.html', {'produk': PRODUCTS})


def detail_produk(request, id):
    produk = next((p for p in PRODUCTS if p['id'] == id), None)
    related = [p for p in PRODUCTS if p['id'] != id][:3]
    return render(request, 'produk/detail_produk.html', {
        'produk': produk,
        'related': related,
    })


def kontak(request):
    return render(request, 'produk/kontak.html')