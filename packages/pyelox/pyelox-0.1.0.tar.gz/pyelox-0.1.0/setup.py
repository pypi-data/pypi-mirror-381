import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyelox",
    version="0.1.0",
    author="GuestRoblox Studios",
    author_email="maria.gomes23.1949@gmail.com",
    description="A minimalist, secure, and compact Python web framework.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["tests"]),
    include_package_data=True,
    keywords='web framework, python, minimalist, micro-framework, secure, security, http, socket, low-level, high-performance, compact, routing, templating, wsgi, asgi, server, pyelox, API, Rest, development, app, fast, reliable, lightweight, production, async, concurrency, scalable, router, middleware, security-focused, easy-to-use, utility, library, web-development, backend',
    install_requires=[
        "python-dotenv",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Science/Research",
        
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Utilities",
        "Topic :: System :: Networking",
        "Topic :: Security",
        
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        
        "Operating System :: OS Independent",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
    ],
    python_requires='>=3.8',
)
