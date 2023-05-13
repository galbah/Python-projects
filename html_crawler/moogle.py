import pickle
from urllib.parse import urljoin
import sys
import requests
import bs4
from pickle import dump
from copy import deepcopy



def link_counter(dict, base_url) :
    """
    a helper for crawl function
    :param dict: dictionary of url's
    :param base_url: the base url of the sites we count the linkes in
    :return: dictionary of dictionary's that describes hoe much time each url contains links to other urls
    """
    for key in dict :
        full_url = urljoin(base_url, key)
        response = requests.get(full_url)
        html = response.text
        soup = bs4.BeautifulSoup(html, 'html.parser')
        for p in soup.find_all("p"):
            for link in p.find_all("a") :
                if link['href'] in dict[key] :
                    dict[key][link['href']] += 1
    return dict



def crawl(base_url, index_file, out_file) :
    """
    :param base_url: the base url we want to crawl in
    :param index_file: file contains all relevant urls we crawl in
    :param out_file: the name of file that the produced dict is saved in
    :return: None
    but saves as file : dictionary of dictionary's that describes hoe much time each url contains links to other urls
    """

    index = open(index_file, 'r')
    traffic_dict = {}
    for line in index :
        traffic_dict[line.replace('\n', '')] = 0

    temp_dict = deepcopy(traffic_dict)
    for link in traffic_dict:
        inner_dict = deepcopy(temp_dict)
        traffic_dict[link] = inner_dict

    traffic_dict = link_counter(traffic_dict, base_url)

    for key in traffic_dict :  # removes keys with value 0
        traffic_dict[key] = {k:v for k,v in traffic_dict[key].items() if v != 0}

    with open(out_file, 'wb') as f :
        dump(traffic_dict, f)



def page_rank_round(dict_file, rank_dict) :
    """
    a helper function for page rank, this function is every iteration of the page ranking
    :param dict_file: dict contains urls and the amount of links between them
    :param rank_dict: the current rank after last round
    :return: the new rank after 1 iteration
    """

    end_round_rank = dict()
    for key in dict_file :
        end_round_rank[key] = 0

    for key in dict_file :
        inner_dict = dict(dict_file[key])
        sum_links = 0
        for inner_key in inner_dict :
            sum_links += inner_dict[inner_key]
        for inner_key in inner_dict :
            points_ratio = inner_dict[inner_key] / sum_links
            points_devided = rank_dict[key] * points_ratio
            end_round_rank[inner_key] += points_devided

    return end_round_rank



def page_rank(iterations, dict_file, out_file) :
    """
    :param iterations: number of rounds that the rank calculation is made
    :param dict_file: dict of dicts describes the links between all urls
    :param out_file: the name of file that the produced dict will be saved in
    :return: None
    but saves as file : a dict that contains rank for every url based on how much links it has on other urls
    """

    dict_file = pickle.load(open(dict_file, 'rb'))
    rank_dict = {}
    for key in dict_file :
        rank_dict[key] = 1

    for round in range(int(iterations)) :
        rank_dict = page_rank_round(dict_file, rank_dict)
        print(rank_dict)

    with open(out_file, 'wb') as f :
        dump(rank_dict, f)



def words_dict(base_url, index_file, out_file) :
    """
    :param base_url: base url of sites that the function should scan all words from
    :param index_file: file contains relative urls that the function should scan all words from
    :param out_file: the name of file that the produced dict will be saved in
    :return: None
    but saves as a file : dict of dicts describes all words from url's and in witch site they ar found and how much times
    """

    words_dict = {}
    index = open(index_file, 'r')
    url_dict = {}
    for line in index:
        url_dict[line.replace('\n', '')] = 0
    temp_dict = {}

    for key in url_dict :
        full_url = urljoin(base_url, key)
        response = requests.get(full_url)
        html = response.text
        soup = bs4.BeautifulSoup(html, 'html.parser')
        for p in soup.find_all("p"):
            splited_content = p.text.split()
            for i in range(len(splited_content)):
                cur_word = splited_content[i]
                if cur_word not in words_dict :
                    temp_dict[key] = 1
                    words_dict[cur_word] = temp_dict
                    temp_dict = {}
                else :
                    if key in words_dict[cur_word] :
                        words_dict[cur_word][key] += 1
                    else:
                        words_dict[cur_word][key] = 1

    with open(out_file, 'wb') as f :
        dump(words_dict, f)


def is_it_in(splited_words, url, word_dict) :
    """
    a helper function for search that checks witch words from 'words' are in the url
    :param words: the words to search as a list
    :param url: te url that is searched in
    :param word_dict: a word dict contains witch words are in witch url's
    :return: list of words from 'words' that is in the url given
    """

    exs_words = []
    length = len(splited_words)

    for i in range(length) :
        cur_word = splited_words[i]
        if cur_word in word_dict and url in word_dict[cur_word] :
            exs_words.append(cur_word)

    return exs_words




def search(query, ranking_dict, words_dict, max_results) :
    """
    :param query: words that the function search
    :param ranking_dict: the ranking dict of all url's made in previous function
    :param words_dict: a dict contains every word in the url's and how much is shows in each site
    :param max_results: max sites printed by the function in the results part
    :return: None
    prints : the 'max_results' url's that contain words or part of them, sorted by there rank that is printed also
    """

    with open(ranking_dict, 'rb') as f:
        ranking_dict= pickle.load(f)

    with open(words_dict, 'rb') as t:
        words_dict = pickle.load(t)

    splited_words = query.split()
    for i in range(len(splited_words)) :
        if splited_words[i] not in words_dict :
            splited_words.remove(splited_words[i])

    relevant_urls = {}
    exs_word_dict = {}
    url_counter = 0
    for key in ranking_dict :
        exs_words = is_it_in(splited_words, key, words_dict)
        if exs_words == splited_words :
            relevant_urls[key] = ranking_dict[key]
            exs_word_dict[key] = exs_words
            url_counter += 1

    relevant_urls = dict(sorted(relevant_urls.items(), key=lambda item: item[1], reverse=True))
    while url_counter > int(max_results) :
        x = relevant_urls.popitem()
        url_counter -= 1

    calc_rank = {}
    splited_words = query.split()
    for key in relevant_urls :
        if len(exs_word_dict[key]) != 1 :
            first_word = exs_word_dict[key][0]
            min = words_dict[first_word][key]
            for i in range(0, len(exs_word_dict[key])) :
                if words_dict[exs_word_dict[key][i]][key] < min :
                    min = words_dict[splited_words[i]][key]
            word_score = min
        else:
            word_score = words_dict[exs_word_dict[key][0]][key]
        url_score = ranking_dict[key]
        calc_rank[key] = word_score * url_score

    calc_rank = dict(sorted(calc_rank.items(), key=lambda item: item[1], reverse=True))

    for key in calc_rank :
        print(key +" "+ str(calc_rank[key]))



if __name__ == "__main__" :

    if sys.argv[1] == "crawl" :
        base_url = sys.argv[2]
        index_file = sys.argv[3]
        out_file = sys.argv[4]
        crawl(base_url, index_file, out_file)

    elif sys.argv[1] == "page_rank" :
        iterations = sys.argv[2]
        dict_file = sys.argv[3]
        out_file = sys.argv[4]
        page_rank(iterations, dict_file, out_file)

    elif sys.argv[1] == "words_dict" :
        base_url = sys.argv[2]
        index_file = sys.argv[3]
        out_file = sys.argv[4]
        words_dict(base_url, index_file, out_file)

    elif sys.argv[1] == "search" :
        query = sys.argv[2]
        ranking_dict_file = sys.argv[3]
        words_dict_file = sys.argv[4]
        max_results = sys.argv[5]
        search(query, ranking_dict_file, words_dict_file, max_results)