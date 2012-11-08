#
# spec file for package perl-gettext
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#



Name:           perl-gettext
Version:        1.05
Release:        151
License:        Artistic-1.0 ; GPL-2.0+
%define cpan_name gettext
Summary:        Message handling functions
Url:            http://search.cpan.org/dist/gettext/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/P/PV/PVANDRY/gettext-%{version}.tar.gz
Patch0:         %{name}-%{version}-POSIX.diff
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
The gettext module permits access from perl to the gettext() family of
functions for retrieving message strings from databases constructed to
internationalize software.

gettext(), dgettext(), and dcgettext() attempt to retrieve a string
matching their 'msgid' parameter within the context of the current locale.
dcgettext() takes the message's category and the text domain as parameters
while dcgettext() defaults to the LC_MESSAGES category and gettext()
defaults to LC_MESSAGES and uses the current text domain. If the string is
not found in the database, then 'msgid' is returned.

textdomain() sets the current text domain and returns the previously active
domain.

_bindtextdomain(domain, dirname)_ instructs the retrieval functions to look
for the databases belonging to domain 'domain' in the directory 'dirname'

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(644,root,root,755)
%doc README

%changelog
